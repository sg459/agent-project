# Assignment-07-Tracker: Spatial Integration and Zonal Statistics

| Field          | Value                                           |
| -------------- | ----------------------------------------------- |
| **Assignment** | 07 — Spatial Integration and Zonal Statistics   |
| **Author**     | Ganbat ([@ganbat3](https://github.com/ganbat3)) |
| **Date**       | 2026-03-17                                      |
| **Status**     | **Completed**                                   |
| **Branch**     | `feature/assignment-07-zonal-stats` → `main`    |

---

## Summary

This assignment computes zonal statistics by extracting raster values (NDVI, soil) for field polygons, performing spatial joins to attach soil health data, and creating multi-layer visualizations for agricultural analysis.

---

## Tasks Completed

### Data Preparation

| Task                           | Status  | Notes                                               |
| ------------------------------ | ------- | --------------------------------------------------- |
| Create field boundary polygons | ✅ Done | 20 fields from weather data centroids (EPSG:4326)   |
| Create soil data CSV           | ✅ Done | 20 records with clay, sand, silt, OM, pH, AWC, kSat |
| Create NDVI raster             | ✅ Done | Synthetic NDVI (EPSG:5070, 500x500 pixels)          |
| Verify CRS alignment           | ✅ Done | Fields reprojected from EPSG:4326 to EPSG:5070      |

### Zonal Statistics (rasterstats library)

| Task                                                    | Status  | Notes                                              |
| ------------------------------------------------------- | ------- | -------------------------------------------------- |
| Calculate mean NDVI per field using `rasterstats`       | ✅ Done | `mean_ndvi` column added (range: 0.415 - 0.726)    |
| Calculate additional NDVI stats (std, min, max, median) | ✅ Done | All stored in GeoDataFrame                         |
| Perform spatial join to attach soil data                | ✅ Done | Used `gpd.sjoin_nearest()` to match soil to fields |
| Merge all zonal statistics into single dataset          | ✅ Done | 20 fields with 27 variables                        |

### Visualization & Mapping

| Task                               | Status  | Output                                                    |
| ---------------------------------- | ------- | --------------------------------------------------------- |
| Multi-layer overlay map (3 layers) | ✅ Done | `07_multilayer_map.png`                                   |
| Integrated dashboard (4 panels)    | ✅ Done | `output/dashboard_assets/integrated_spatial_analysis.png` |
| Correlation heatmap                | ✅ Done | `07_zonal_correlation.png`                                |

### Output Files Generated

```
data/
├── fields/ohio_maumee_20.geojson
├── soil/ohio_maumee_20_soil.csv
└── ndvi/ohio_maumee_2023_ndvi.tif

output/
├── zonal_statistics_summary.csv
├── zonal_statistics_fields.geojson
├── zonal_stats_rasterstats.csv
├── zonal_stats_rasterstats.geojson
├── 07_zonal_correlation.png
├── 07_multilayer_map.png
└── dashboard_assets/
    └── integrated_spatial_analysis.png
```

---

## Key Findings: Zonal Statistics Results

### NDVI Statistics by Field

| Statistic | Value |
| --------- | ----- |
| Mean NDVI | 0.584 |
| Std Dev   | 0.274 |
| Min       | 0.415 |
| Max       | 0.726 |

### Soil Properties Summary

| Property | Mean | Min  | Max  |
| -------- | ---- | ---- | ---- |
| Clay (%) | 23.7 | 15.7 | 33.8 |
| Sand (%) | 45.3 | 31.5 | 58.7 |
| OM (%)   | 2.6  | 1.5  | 4.0  |
| pH       | 6.4  | 5.5  | 7.1  |

### Field Classification

- **High clay soils (>25%):** 8 fields (blue border in map)
- **Low clay soils (≤25%):** 12 fields (orange border in map)

---

## Weather Data Integration

### Weather Data Source

- **File:** `data/weather/ohio_maumee_20_2020_2023.csv`
- **Records:** 29,220 daily observations (20 fields × 4 years × 365 days)
- **Variables:** T2M, T2M_MAX, T2M_MIN, PRECTOTCORR, ALLSKY_SFC_SW_DWN, RH2M

### Weather Data Quality Notes

| Issue                    | Handling                                           |
| ------------------------ | -------------------------------------------------- |
| Sentinel values (-999)   | Replaced with NaN using `.replace(-999.0, np.nan)` |
| Missing field boundaries | Created from weather data centroids                |
| Missing soil data        | Generated synthetic soil data for 20 fields        |
| Missing NDVI rasters     | Created synthetic NDVI raster for analysis         |

### Weather Trends Documentation

> **Note:** Detailed weather trend analysis (including the 2023 drought) was completed in **Assignment-06-Tracker**. For this spatial integration assignment, weather data was aggregated to field level but the primary focus was on NDVI and soil zonal statistics.

For the complete weather analysis findings (including severe drought conditions), see: `docs/project/assignment-06-tracker.md`

---

## Validation

- ✅ Notebook JSON is valid (34 cells)
- ✅ All cells execute without errors
- ✅ All output files generated successfully
- ✅ CRS alignment verified between all layers

---

## Related Documentation

- Field boundaries: `data/fields/ohio_maumee_20.geojson`
- Soil data: `data/soil/ohio_maumee_20_soil.csv`
- NDVI raster: `data/ndvi/ohio_maumee_2023_ndvi.tif`
- Weather data: `data/weather/ohio_maumee_20_2020_2023.csv`
- Previous weather analysis: `docs/project/assignment-06-tracker.md`
