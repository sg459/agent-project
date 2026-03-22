# Assignment-08-Tracker: Soil Health and Sustainability Analysis

| Field          | Value                                           |
| -------------- | ----------------------------------------------- |
| **Assignment** | 08 — Soil Health and Sustainability Analysis    |
| **Author**     | Ganbat ([@ganbat3](https://github.com/ganbat3)) |
| **Date**       | 2026-03-21                                      |
| **Status**     | **Completed**                                   |
| **Branch**     | `feature/assignment-08-soil-health` → `main`    |

---

## Summary

This assignment analyzes soil health indicators and sustainability metrics for the 20 Maumee watershed fields. Key analyses include filtering key soil health indicators (OM, pH, CEC), calculating soil health scores, assessing erosion risk using K-factor, and creating comprehensive visualizations for the final dashboard.

---

## Tasks Completed

### Data Preparation & Exploration

| Task                                    | Status  | Notes                                               |
| --------------------------------------- | ------- | --------------------------------------------------- |
| Load field boundaries                   | ✅ Done | 20 fields from `ohio_maumee_20.geojson` (EPSG:4326) |
| Load soil data (SSURGO)                 | ✅ Done | 20 records with clay, sand, silt, OM, pH, AWC, kSat |
| Filter for key indicators (OM, pH, CEC) | ✅ Done | Created `ohio_maumee_20_soil_health.csv`            |

### Soil Health Scoring

| Task                                     | Status  | Notes                                      |
| ---------------------------------------- | ------- | ------------------------------------------ |
| Calculate CEC (estimated from clay + OM) | ✅ Done | Formula: `CEC = (clay% × 0.5) + (OM% × 2)` |
| Normalize indicators to 0-100 scale      | ✅ Done | OM, pH, and CEC scored                     |
| Calculate composite Soil Health Score    | ✅ Done | Weighted: OM (40%), pH (30%), CEC (30%)    |
| Group by Field ID and rank               | ✅ Done | Top field: 391623004305517 (Score: 90.8)   |
| Save soil health scores                  | ✅ Done | `ohio_maumee_20_soil_health_scores.csv`    |

### Erosion Risk Assessment

| Task                                  | Status  | Notes                                        |
| ------------------------------------- | ------- | -------------------------------------------- |
| Calculate K-Factor (soil erodibility) | ✅ Done | Using particle size distribution formula     |
| Calculate infiltration risk (kSat)    | ✅ Done | Low kSat = higher erosion risk               |
| Calculate OM-based erosion risk       | ✅ Done | Lower OM = higher erosion risk               |
| Combined erosion risk score           | ✅ Done | K-Factor (40%), Infiltration (30%), OM (30%) |
| Identify high-risk fields             | ✅ Done | 3 fields with erosion risk > 70              |
| Save erosion risk data                | ✅ Done | `ohio_maumee_20_erosion_risk.csv`            |

### Visualization & Analysis

| Task                                   | Status  | Output                                            |
| -------------------------------------- | ------- | ------------------------------------------------- |
| OM comparison: Top 10 vs Bottom 10     | ✅ Done | `08_om_by_productivity.png`                       |
| Spatial drainage class map             | ✅ Done | `08_drainage_classes_spatial.png`                 |
| Soil Health & Sustainability Dashboard | ✅ Done | `08_soil_health_dashboard.png`                    |
| Final dashboard in dashboard_assets    | ✅ Done | `output/dashboard_assets/soil_health_metrics.png` |

---

## Key Findings: Soil Health Analysis

### Soil Health Score Distribution

| Statistic  | Value                        |
| ---------- | ---------------------------- |
| Mean Score | 54.7                         |
| Min Score  | 29.4 (field 391623004291427) |
| Max Score  | 90.8 (field 391623004305517) |

### Top 5 Fields (Highest Soil Health)

| Field ID        | OM (%) | pH  | CEC  | Score |
| --------------- | ------ | --- | ---- | ----- |
| 391623004305517 | 3.96   | 6.0 | 20.9 | 90.8  |
| 391623004305230 | 3.31   | 7.0 | 23.5 | 86.3  |
| 391623000245868 | 3.27   | 5.5 | 22.9 | 81.0  |
| 391623000245685 | 3.33   | 6.5 | 18.1 | 76.7  |
| 391623004303760 | 3.49   | 5.9 | 17.2 | 73.5  |

---

## Most Common Soil Limitations

### Drainage Class Distribution

| Drainage Class          | Count | Percentage |
| ----------------------- | ----- | ---------- |
| Moderately Well Drained | 10    | 50%        |
| Somewhat Poorly Drained | 5     | 25%        |
| Well Drained            | 4     | 20%        |
| Poorly Drained          | 1     | 5%         |

> **Key Finding:** **50% of fields are limited by moderately well-drained conditions**, with 30% having some level of drainage restriction (Somewhat Poorly Drained + Poorly Drained = 30%). These conditions can affect nutrient availability, field workability, and crop selection.

### Erosion Risk Distribution

| Risk Level       | Count | Percentage |
| ---------------- | ----- | ---------- |
| High Risk (>70)  | 3     | 15%        |
| Moderate (40-70) | 12    | 60%        |
| Low Risk (<40)   | 5     | 25%        |

> **Key Finding:** **75% of fields have moderate to high erosion risk**, primarily due to low organic matter content (mean OM: 2.6%) and varying infiltration rates. The 3 highest-risk fields all have OM < 1.7%.

---

## Sustainability Metrics Tracked

| Metric                  | Description                                 | Range/Values  |
| ----------------------- | ------------------------------------------- | ------------- |
| **Soil Health Score**   | Composite of OM, pH, CEC (0-100 scale)      | 29.4 - 90.8   |
| **Organic Matter (%)**  | Soil organic carbon content                 | 1.53% - 3.96% |
| **pH**                  | Soil acidity/alkalinity                     | 5.5 - 7.1     |
| **CEC (meq/100g)**      | Cation Exchange Capacity (nutrient holding) | 10.9 - 23.5   |
| **Erosion Risk Score**  | K-Factor + infiltration + OM (0-100 scale)  | 17.5 - 81.9   |
| **K-Factor**            | Soil erodibility index                      | 0.086 - 0.093 |
| **Drainage Class**      | Soil drainage classification                | 4 categories  |
| **Productivity (NDVI)** | Vegetation index as yield proxy             | 0.415 - 0.726 |

---

## Output Files Generated

```
data/
├── soil/
│   ├── ohio_maumee_20_soil.csv
│   ├── ohio_maumee_20_soil_health.csv
│   ├── ohio_maumee_20_soil_health_scores.csv
│   └── ohio_maumee_20_erosion_risk.csv
├── fields/ohio_maumee_20.geojson
├── ndvi/ohio_maumee_2023_ndvi.tif

output/
├── 08_om_by_productivity.png
├── 08_drainage_classes_spatial.png
├── 08_soil_health_dashboard.png
└── dashboard_assets/
    └── soil_health_metrics.png
```

---

## Validation

- ✅ Notebook JSON is valid
- ✅ All cells execute without errors
- ✅ All output files generated successfully
- ✅ CRS alignment verified

---

## Related Documentation

- Field boundaries: `data/fields/ohio_maumee_20.geojson`
- Soil data: `data/soil/ohio_maumee_20_soil.csv`
- Previous assignment: `docs/project/assignment-07-tracker.md`
