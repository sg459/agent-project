# Agricultural Data Analysis Skills

A collection of AI-ready skills for downloading and analyzing US agricultural data using standard Python libraries.

## Quick Start

```bash
# Install UV (fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# All skills use UV for isolated environments
# Example: Download field boundaries
cd field-boundaries
uv run --with geopandas python << 'EOF'
from field_boundaries import download_fields
fields = download_fields(count=2, regions=['corn_belt'])
fields.to_file('my_fields.geojson')
EOF
```

## Skills Overview

### Data Download Skills (With Python Code + Examples)

All data download skills include:

- **Real code**: Standard Python libraries (no custom wrappers)
- **Examples/**: Sample data for 2 real fields from Minnesota
- **SKILL.md**: AgentSkills.io format with YAML frontmatter
- **UV isolation**: Each skill runs in its own environment

| Skill                   | Description                        | Dependencies                |
| ----------------------- | ---------------------------------- | --------------------------- |
| **field-boundaries**    | USDA NASS Crop Sequence Boundaries | geopandas, matplotlib       |
| **ssurgo-soil**         | USDA NRCS SSURGO soil data         | geopandas, pandas, requests |
| **nasa-power-weather**  | NASA POWER weather data            | pandas, requests, xarray    |
| **cdl-cropland**        | USDA NASS Cropland Data Layer      | rasterio, geopandas         |
| **sentinel2-imagery**   | ESA Sentinel-2 satellite imagery   | sentinelsat, rasterio       |
| **landsat-imagery**     | USGS Landsat satellite imagery     | landsatxplore, rasterio     |
| **interactive-web-map** | Interactive web maps               | folium, geopandas           |

### Analysis Skills (Markdown + Code Examples)

These skills teach standard Python libraries:

| Skill               | Purpose              | Libraries                   |
| ------------------- | -------------------- | --------------------------- |
| **eda-explore**     | Data exploration     | pandas, numpy               |
| **eda-visualize**   | Data visualization   | pandas, matplotlib, seaborn |
| **eda-correlate**   | Correlation analysis | pandas, scipy               |
| **eda-time-series** | Time series analysis | pandas, matplotlib          |
| **eda-compare**     | Group comparisons    | pandas, scipy               |

## Example Data

All data download skills include minimal real data for testing:

```
.skills/
├── field-boundaries/examples/sample_2_fields.geojson  # 2 real MN fields
├── ssurgo-soil/examples/soil_data_2_fields.csv        # Soil for those fields
├── nasa-power-weather/examples/sample_weather_2fields_2020_2024.csv
├── cdl-cropland/examples/sample_cdl_2_fields.csv
└── ...
```

## Dependency Chain

```
field-boundaries (REQUIRED FIRST)
    │
    ├──> ssurgo-soil (uses field polygons)
    ├──> nasa-power-weather (uses field locations)
    ├──> cdl-cropland (can use fields for AOI)
    ├──> sentinel2-imagery (needs AOI)
    ├──> landsat-imagery (needs AOI)
    └──> interactive-web-map (visualizes fields)

eda-* skills (independent - work with any CSV)
```

## Repository Sync

These skills are synced to [ag-skills](https://github.com/borealBytes/ag-skills) for student access.

**Sync mechanism**: Git subtree

- Changes to `.skills/` in this repo → auto-sync to ag-skills
- Students get only the skills, not course materials

## Agent Skills Format

All skills follow [AgentSkills.io](https://agentskills.io) format:

```yaml
---
name: skill-name
description: Clear description
version: 1.0.0
author: Boreal Bytes
tags: [agriculture, data, ...]
---
# Skill Content
- Description
- When to Use
- Prerequisites (UV)
- Quick Start
- Usage Examples
- Data Source
```

## License

MIT License - See [THIRD_PARTY_NOTICES.md](../../../THIRD_PARTY_NOTICES.md)

## UV Usage

All skills use [UV](https://github.com/astral-sh/uv) for isolated Python environments. This ensures reproducible, sandboxed execution without conflicting dependencies.

### Installing UV

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

### Running Skill Scripts

Each skill can be run in isolation using `uv run`:

```bash
# Run a skill script with dependencies
cd field-boundaries
uv run --with geopandas,matplotlib python -c "
from field_boundaries import download_fields
fields = download_fields(count=2, regions=['corn_belt'])
fields.to_file('my_fields.geojson')
"

# Or run with a script file
uv run --with geopandas,matplotlib scripts/example.py
```

### Per-Skill Dependencies

Each skill specifies its own dependencies in the script or SKILL.md. Common dependencies:

| Skill               | Dependencies                |
| ------------------- | --------------------------- |
| field-boundaries    | geopandas, matplotlib       |
| ssurgo-soil         | geopandas, pandas, requests |
| nasa-power-weather  | pandas, requests, xarray    |
| cdl-cropland        | rasterio, geopandas         |
| sentinel2-imagery   | sentinelsat, rasterio       |
| landsat-imagery     | landsatxplore, rasterio     |
| interactive-web-map | folium, geopandas           |
| eda-explore         | pandas, numpy               |
| eda-visualize       | pandas, matplotlib, seaborn |
| eda-correlate       | pandas, scipy               |
| eda-time-series     | pandas, matplotlib          |
| eda-compare         | pandas, scipy               |

### Updating Skills from Upstream

```bash
git subtree pull --prefix=.skills/ag-skills ag-skills skills-content --squash
```

## Citation

```
USDA National Agricultural Statistics Service Cropland Data Layer. 2023.
Published crop-specific data layer [Online].
Available at https://nassgeodata.gmu.edu/CropScape/
```
