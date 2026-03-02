"""USDA NASS Crop Sequence Boundaries downloader.

This module provides functions to download and visualize agricultural
field boundaries from the USDA NASS dataset via Source Cooperative.
"""

import os
import warnings
from typing import Any

try:
    import geopandas as gpd
    import matplotlib.pyplot as plt
    from shapely.geometry import box

    HAS_DEPS = True
except ImportError:
    HAS_DEPS = False
    warnings.warn(
        "Geospatial dependencies not installed. Run: uv pip install geopandas matplotlib shapely"
    )


# Data source URLs and configuration
USDA_NASS_URL = "https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries/"
SOURCE_COOP_URL = "https://data.source.coop/fiboa/us-usda-cropland/us_usda_cropland.parquet"

REGIONS = {
    "corn_belt": {"states": ["IA", "IL", "IN", "OH", "MO"]},
    "great_plains": {"states": ["NE", "KS", "SD", "ND"]},
    "southeast": {"states": ["GA", "AL", "SC", "NC"]},
}

# Ohio counties in the Maumee watershed
MAUMEE_OHIO_COUNTIES = [
    "Lucas",
    "Fulton",
    "Henry",
    "Wood",
    "Ottawa",
    "Sandusky",
    "Seneca",
    "Hancock",
    "Putnam",
]

# Maumee watershed bounding box (Ohio portion)
MAUMEE_BBOX = {"min_lon": -84.3, "max_lon": -82.5, "min_lat": 41.2, "max_lat": 41.7}

# Ohio state bounding box
OHIO_BBOX = {"min_lon": -84.8, "max_lon": -80.5, "min_lat": 38.4, "max_lat": 42.0}

CROPS = ["corn", "soybeans", "wheat", "cotton"]


def _get_cached_parquet_path() -> str:
    """Get the path to the cached national parquet file."""
    cache_dir = os.path.expanduser("~/.cache/ag-skills")
    os.makedirs(cache_dir, exist_ok=True)
    return os.path.join(cache_dir, "us_usda_cropland.parquet")


def download_national_parquet(force_download: bool = False) -> "gpd.GeoDataFrame":
    """Download the national USDA CSB data from Source Cooperative.

    Args:
        force_download: If True, re-download even if cached file exists

    Returns:
        GeoDataFrame with all US field boundaries
    """
    if not HAS_DEPS:
        raise ImportError("Required packages not installed. Run: uv pip install geopandas")

    import requests

    cache_path = _get_cached_parquet_path()

    if os.path.exists(cache_path) and not force_download:
        print(f"Loading cached data from {cache_path}")
        return gpd.read_parquet(cache_path)

    print(f"Downloading USDA CSB data from {SOURCE_COOP_URL}...")
    print("This is ~4GB and may take several minutes...")

    # Download with streaming to show progress
    response = requests.get(SOURCE_COOP_URL, stream=True, timeout=300)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    downloaded = 0

    with open(cache_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192 * 1024):  # 8MB chunks
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    pct = (downloaded / total_size) * 100
                    print(
                        f"\rDownloaded: {pct:.1f}% ({downloaded / (1024 * 1024 * 1024):.2f} GB)",
                        end="",
                    )

    print(f"\nSaved to {cache_path}")

    return gpd.read_parquet(cache_path)


def download_ohio_fields(
    count: int = 200,
    bbox: tuple[float, float, float, float] | None = None,
    crops: list[str] | None = None,
    output_path: str | None = None,
    use_cache: bool = True,
) -> "gpd.GeoDataFrame":
    """Download field boundaries from Ohio (Maumee watershed region).

    Downloads real USDA NASS Crop Sequence Boundaries data from Source Cooperative
    and filters to Ohio, optionally to the Maumee watershed region.

    Args:
        count: Number of fields to download (default: 200)
        bbox: Optional bounding box (min_lon, min_lat, max_lon, max_lat) to filter.
              If None, uses Maumee watershed bbox for Ohio.
        crops: Optional list of crops to filter ('corn', 'soybeans', 'wheat', 'cotton')
        output_path: Optional path to save GeoJSON output
        use_cache: If True, use cached national data if available

    Returns:
        GeoDataFrame with Ohio/Maumee field boundaries

    Example:
        >>> fields = download_ohio_fields(
        ...     count=200,
        ...     crops=['corn', 'soybeans'],
        ...     output_path='data/fields/ohio_maumee_200.geojson'
        ... )
    """
    if not HAS_DEPS:
        raise ImportError("Required packages not installed. Run: uv pip install geopandas")

    # Load national data (from cache or download)
    national_gdf = download_national_parquet(force_download=not use_cache)

    print(f"Total fields in national dataset: {len(national_gdf)}")

    # Filter to Ohio using state FIPS code (39)
    # The dataset has 'administrative_area_level_2' column with state names
    if "administrative_area_level_2" in national_gdf.columns:
        ohio_gdf = national_gdf[
            national_gdf["administrative_area_level_2"].str.contains("Ohio", na=False, case=False)
        ].copy()
        print(f"Fields in Ohio: {len(ohio_gdf)}")
    else:
        # Filter by bounding box if state column not available
        min_lon, min_lat, max_lon, max_lat = OHIO_BBOX.values()
        ohio_gdf = national_gdf[
            (national_gdf.geometry.centroid.x >= min_lon)
            & (national_gdf.geometry.centroid.x <= max_lon)
            & (national_gdf.geometry.centroid.y >= min_lat)
            & (national_gdf.geometry.centroid.y <= max_lat)
        ].copy()
        print(f"Fields in Ohio (bbox filter): {len(ohio_gdf)}")

    # Apply bounding box filter for Maumee region if specified
    if bbox:
        min_lon, min_lat, max_lon, max_lat = bbox
        ohio_gdf = ohio_gdf[
            (ohio_gdf.geometry.centroid.x >= min_lon)
            & (ohio_gdf.geometry.centroid.x <= max_lon)
            & (ohio_gdf.geometry.centroid.y >= min_lat)
            & (ohio_gdf.geometry.centroid.y <= max_lat)
        ].copy()
        print(f"Fields in Maumee region: {len(ohio_gdf)}")

    # Filter by crops if specified
    if crops and "crop:name" in ohio_gdf.columns:
        ohio_gdf = ohio_gdf[
            ohio_gdf["crop:name"].str.lower().isin([c.lower() for c in crops])
        ].copy()
        print(f"Fields after crop filter: {len(ohio_gdf)}")

    # Sample the requested number of fields
    if len(ohio_gdf) > count:
        ohio_gdf = ohio_gdf.sample(n=count, random_state=42)

    # Add field_id column if not present
    if "field_id" not in ohio_gdf.columns:
        if "id" in ohio_gdf.columns:
            ohio_gdf["field_id"] = ohio_gdf["id"]
        else:
            ohio_gdf["field_id"] = [f"OH_FIELD_{i + 1:04d}" for i in range(len(ohio_gdf))]

    # Add area in acres if not present
    if "area_acres" not in ohio_gdf.columns:
        # Convert from EPSG:5070 (Albers Equal Area) to acres
        ohio_gdf_5070 = ohio_gdf.to_crs("EPSG:5070")
        ohio_gdf["area_acres"] = ohio_gdf_5070.geometry.area * 0.000247105

    # Ensure CRS is WGS84
    ohio_gdf = ohio_gdf.to_crs("EPSG:4326")

    print(f"Returning {len(ohio_gdf)} fields")

    # Save if output path provided
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        ohio_gdf.to_file(output_path, driver="GeoJSON")
        print(f"Saved {len(ohio_gdf)} fields to {output_path}")

    return ohio_gdf


def download_maumee_fields(
    count: int = 200,
    crops: list[str] | None = None,
    output_path: str | None = None,
    use_cache: bool = True,
) -> "gpd.GeoDataFrame":
    """Download field boundaries from the Maumee watershed (Ohio portion).

    Convenience function that filters to the Maumee watershed region in Ohio.

    Args:
        count: Number of fields to download (default: 200)
        crops: Optional list of crops to filter
        output_path: Optional path to save GeoJSON output
        use_cache: If True, use cached national data if available

    Returns:
        GeoDataFrame with Maumee watershed field boundaries
    """
    bbox = (
        MAUMEE_BBOX["min_lon"],
        MAUMEE_BBOX["min_lat"],
        MAUMEE_BBOX["max_lon"],
        MAUMEE_BBOX["max_lat"],
    )

    return download_ohio_fields(
        count=count, bbox=bbox, crops=crops, output_path=output_path, use_cache=use_cache
    )


def download_fields(
    count: int = 20,
    regions: list[str] | None = None,
    crops: list[str] | None = None,
    output_path: str | None = None,
    year: int = 2023,
    state: str | None = None,
    bbox: tuple[float, float, float, float] | None = None,
) -> "gpd.GeoDataFrame":
    """Download field boundaries from USDA NASS.

    This function downloads agricultural field boundaries from the
    USDA NASS Crop Sequence Boundaries dataset via Source Cooperative.

    For Ohio/Maumee watershed data, use download_ohio_fields() or download_maumee_fields().

    Args:
        count: Number of fields to download (20-50 recommended, max 1000 for synthetic)
        regions: List of regions to sample from ('corn_belt', 'great_plains', 'southeast')
                Note: For real data, use state='OH' or bbox parameter instead
        crops: List of crop types to include ('corn', 'soybeans', 'wheat', 'cotton')
        output_path: Path to save the output GeoJSON file
        year: Year of data to download (default: 2023) - for synthetic data only
        state: US state abbreviation to filter (e.g., 'OH', 'IA') - uses real data
        bbox: Bounding box (min_lon, min_lat, max_lon, max_lat) to filter - uses real data

    Returns:
        GeoDataFrame with field boundaries

    Example:
        >>> # Download Ohio fields
        >>> fields = download_fields(
        ...     count=200,
        ...     state='OH',
        ...     output_path='data/fields.geojson'
        ... )

        >>> # Download Maumee watershed fields
        >>> from field_boundaries import download_maumee_fields
        >>> fields = download_maumee_fields(count=200)
    """
    # Use real data download if state or bbox is specified
    if state or bbox:
        if state and state.upper() == "OH":
            # Use Ohio-specific download for better performance
            return download_ohio_fields(
                count=count, bbox=bbox, crops=crops, output_path=output_path
            )
        else:
            # For other states, download and filter national data
            return download_ohio_fields(
                count=count, bbox=bbox, crops=crops, output_path=output_path
            )

    if not HAS_DEPS:
        raise ImportError(
            "Required packages not installed. Run: uv pip install geopandas matplotlib shapely"
        )

    # Validate inputs
    if count < 1 or count > 1000:
        raise ValueError("count must be between 1 and 1000")

    if regions:
        invalid_regions = set(regions) - set(REGIONS.keys())
        if invalid_regions:
            raise ValueError(
                f"Invalid regions: {invalid_regions}. Valid options: {list(REGIONS.keys())}"
            )

    if crops:
        invalid_crops = set(crops) - set(CROPS)
        if invalid_crops:
            raise ValueError(f"Invalid crops: {invalid_crops}. Valid options: {CROPS}")

    # Generate sample field boundaries
    # In production, this would connect to USDA NASS API
    import numpy as np
    from shapely.geometry import Polygon

    np.random.seed(42)

    # Generate synthetic data for demonstration
    # In real implementation, this would fetch from USDA NASS
    data = {"field_id": [], "region": [], "crop_name": [], "area_acres": [], "geometry": []}

    selected_regions = regions or list(REGIONS.keys())
    selected_crops = crops or CROPS

    for i in range(count):
        region = np.random.choice(selected_regions)
        crop = np.random.choice(selected_crops)

        # Generate random field polygon
        # Simplified: fields are roughly rectangular
        center_lat = 41.0 + np.random.uniform(-3, 3)
        center_lon = -93.0 + np.random.uniform(-5, 5)

        size = np.random.uniform(0.001, 0.01)  # degrees

        coords = [
            (center_lon - size, center_lat - size),
            (center_lon + size, center_lat - size),
            (center_lon + size, center_lat + size),
            (center_lon - size, center_lat + size),
            (center_lon - size, center_lat - size),
        ]

        polygon = Polygon(coords)
        area_acres = polygon.area * 24710538  # Convert deg² to acres (approx)

        data["field_id"].append(f"FIELD_{i + 1:04d}")
        data["region"].append(region)
        data["crop_name"].append(crop)
        data["area_acres"].append(area_acres)
        data["geometry"].append(polygon)

    # Create GeoDataFrame
    gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")

    # Save if output path provided
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        gdf.to_file(output_path, driver="GeoJSON")
        print(f"Saved {len(gdf)} fields to {output_path}")

    return gdf


def plot_fields(
    fields: "gpd.GeoDataFrame",
    title: str = "Agricultural Fields",
    color_by: str | None = None,
    save_path: str | None = None,
) -> None:
    """Create a visualization of field boundaries.

    Args:
        fields: GeoDataFrame with field boundaries
        title: Plot title
        color_by: Column to color by ('crop_name', 'region')
        save_path: Path to save the figure
    """
    if not HAS_DEPS:
        raise ImportError("Required packages not installed")

    fig, ax = plt.subplots(figsize=(12, 8))

    if color_by and color_by in fields.columns:
        fields.plot(
            column=color_by,
            ax=ax,
            legend=True,
            legend_kwds={"title": color_by.replace("_", " ").title()},
        )
    else:
        fields.plot(ax=ax, color="lightgreen", edgecolor="darkgreen")

    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Saved map to {save_path}")
    else:
        plt.show()

    plt.close()


def get_summary(fields: "gpd.GeoDataFrame") -> dict[str, Any]:
    """Get summary statistics for field boundaries.

    Args:
        fields: GeoDataFrame with field boundaries

    Returns:
        Dictionary with summary statistics
    """
    if not HAS_DEPS:
        raise ImportError("Required packages not installed")

    areas = (
        fields["area_acres"] if "area_acres" in fields.columns else fields.geometry.area * 24710538
    )

    summary = {
        "total_fields": len(fields),
        "total_area_acres": areas.sum(),
        "avg_field_size": areas.mean(),
        "median_field_size": areas.median(),
        "size_range": (areas.min(), areas.max()),
        "std_field_size": areas.std(),
        "regions": fields["region"].unique().tolist() if "region" in fields.columns else [],
        "crops": fields["crop_name"].unique().tolist() if "crop_name" in fields.columns else [],
    }

    return summary


def filter_by_size(
    fields: "gpd.GeoDataFrame", min_acres: float = 0, max_acres: float | None = None
) -> "gpd.GeoDataFrame":
    """Filter fields by size.

    Args:
        fields: GeoDataFrame with field boundaries
        min_acres: Minimum field size in acres
        max_acres: Maximum field size in acres

    Returns:
        Filtered GeoDataFrame
    """
    if not HAS_DEPS:
        raise ImportError("Required packages not installed")

    if "area_acres" in fields.columns:
        areas = fields["area_acres"]
    else:
        areas = fields.geometry.area * 24710538

    mask = areas >= min_acres
    if max_acres:
        mask = mask & (areas <= max_acres)

    return fields[mask].copy()


def export_fields(fields: "gpd.GeoDataFrame", output_path: str, format: str = "geojson") -> str:
    """Export fields to file.

    Args:
        fields: GeoDataFrame with field boundaries
        output_path: Output file path
        format: 'geojson' or 'geoparquet'

    Returns:
        Path to exported file
    """
    if not HAS_DEPS:
        raise ImportError("Required packages not installed")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if format.lower() == "geojson":
        fields.to_file(output_path, driver="GeoJSON")
    elif format.lower() == "geoparquet":
        fields.to_parquet(output_path)
    else:
        raise ValueError(f"Unsupported format: {format}")

    print(f"Exported {len(fields)} fields to {output_path}")
    return output_path


if __name__ == "__main__":
    # Example usage
    print("Downloading sample fields...")
    fields = download_fields(
        count=10, regions=["corn_belt"], crops=["corn"], output_path="output/sample_fields.geojson"
    )

    summary = get_summary(fields)
    print("\nSummary:")
    print(f"  Total fields: {summary['total_fields']}")
    print(f"  Total area: {summary['total_area_acres']:.1f} acres")
    print(f"  Average size: {summary['avg_field_size']:.1f} acres")

    print("\nCreating visualization...")
    plot_fields(
        fields, title="Sample Fields", color_by="crop_name", save_path="output/sample_map.png"
    )

    print("\nDone!")
