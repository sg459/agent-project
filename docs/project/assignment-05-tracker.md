# Assignment-05 Tracker — Vegetation Index (NDVI) Calculation and Crop Health Analysis

_Assignment: Satellite imagery download, band reading, and NDVI calculation_
_Branch: feature/assignment-05-ndvi_
_Last updated: 2026-03-08_

---

## 📋 Task overview

**Goal:** Download real Sentinel-2 satellite imagery for an Ohio Maumee watershed field, read individual spectral bands, calculate NDVI, and produce publication-quality output images demonstrating a working remote sensing pipeline.

**Data source:** Copernicus Data Space — Sentinel-2 L2A, July 2024, 10m resolution

---

## ✅ Task status

| Task                                        | Status      | Notes                                                                   |
| ------------------------------------------- | ----------- | ----------------------------------------------------------------------- |
| Import ag-skills from borealBytes/ag-skills | ✅ Complete | Subtree updated, symlinked to `.claude/skills/` and `.opencode/skills/` |
| Set up credentials securely                 | ✅ Complete | `.env` file (gitignored), loaded via `python-dotenv`                    |
| Authenticate with Copernicus API            | ✅ Complete | OAuth2 client credentials, token verified                               |
| Download Red band (B04)                     | ✅ Complete | 27 KB GeoTIFF, 80x120 px                                                |
| Download NIR band (B08)                     | ✅ Complete | 25 KB GeoTIFF, 80x120 px                                                |
| Read bands with rasterio                    | ✅ Complete | Verified shape, dtype, CRS, bounds                                      |
| Calculate NDVI                              | ✅ Complete | `(NIR - Red) / (NIR + Red)`, saved as GeoTIFF                           |
| Produce single-band output image            | ✅ Complete | NIR band visualization (300 DPI)                                        |
| Produce NDVI output image                   | ✅ Complete | 10-class classified map with legend (300 DPI)                           |
| Write markdown walkthrough                  | ✅ Complete | `reports/assignment-05-walkthrough.md` with inline images               |
| Add cloud/sensor combination note           | ✅ Complete | Scene-level cloud filter; pixel-level SCL masking deferred              |
| Create assignment-05 notebook               | ✅ Complete | `notebooks/05_ndvi_crop_health.ipynb`                                   |

---

## 📁 Inputs, scripts, and outputs

### Inputs used

| File                        | Source                    | Description                               |
| --------------------------- | ------------------------- | ----------------------------------------- |
| `sample_2_fields.geojson`   | `field-boundaries` skill  | 2 sample field boundaries (AOI reference) |
| `sample_aoi.geojson`        | `sentinel2-imagery` skill | Sentinel-2 AOI bounding box               |
| `sample_field_stats.csv`    | `sentinel2-imagery` skill | Example per-field NDVI statistics         |
| `sample_ndvi_metadata.json` | `sentinel2-imagery` skill | Example scene metadata                    |
| `sample_ndvi_pixels.csv`    | `sentinel2-imagery` skill | Example pixel-level NDVI values           |

### Scripts used

| File                                  | Description                                                   |
| ------------------------------------- | ------------------------------------------------------------- |
| `notebooks/05_ndvi_crop_health.ipynb` | Full pipeline: auth, download, read, NDVI calc, visualization |

### Single-band output images

| File                     |   Size | Description                                    |
| ------------------------ | -----: | ---------------------------------------------- |
| `sentinel2_B04_Red.tif`  |  27 KB | Red band reflectance (B04), float32, EPSG:4326 |
| `sentinel2_B08_NIR.tif`  |  25 KB | NIR band reflectance (B08), float32, EPSG:4326 |
| `nir_band_B08.png`       | 210 KB | NIR single-band visualization (300 DPI)        |
| `nir_red_comparison.png` | 312 KB | Side-by-side NIR vs Red comparison (300 DPI)   |

### NDVI output images

| File                 |   Size | Description                                        |
| -------------------- | -----: | -------------------------------------------------- |
| `sentinel2_NDVI.tif` |  43 KB | Calculated NDVI raster, float32, EPSG:4326         |
| `ndvi_map.png`       | 231 KB | 10-class classified NDVI map with legend (300 DPI) |
| `ndvi_histogram.png` | 112 KB | NDVI pixel distribution histogram (300 DPI)        |

All files located under `data/assignment-05/`.

---

## ⚠️ Cloud masking and sensor combination note

**Cloud masking:** Scene-level filter applied (`maxCloudCoverage: 30`). Pixel-level cloud masking via the Sentinel-2 SCL band was intentionally deferred — not needed for a single-date NDVI snapshot.

**Sensor combination:** Single Sentinel-2 scene used. No multi-sensor fusion or multi-date compositing performed. Deferred to future work requiring temporal analysis.

---

## 🔄 Remaining tasks

- [ ] Apply SCL pixel-level cloud mask before NDVI calculation
- [ ] Download multi-date imagery for growing season time series
- [ ] Compute zonal NDVI statistics per field (all 20 fields)
- [ ] Compare Sentinel-2 (10m) with Landsat (30m) cross-sensor
- [ ] Correlate NDVI with soil properties and weather data

---

## ✍️ Progress checklist

- [x] Class template + skills import setup completed
- [x] One imagery data-read run completed
- [x] One single-band output image generated
- [x] One NDVI output image generated
- [x] Markdown walkthrough with inline images added
- [x] Cloud/combination context note added
- [x] Inputs/scripts/outputs captured

---

_Last updated: 2026-03-08_
