# Assignment-02 Tracker — Agricultural Data Pipeline

_Assignment: First Data Download and Visualization_
_Branch: feature/assignment-02-first-data_
_Last updated: 2026-03-01_

---

## 📋 Task Overview

**Goal:** Download agricultural field data for Ohio Maumee watershed, integrate multiple datasets, and create interactive visualization.

**Data Sources:**

- USDA NASS Crop Sequence Boundaries (field boundaries)
- USDA NASS CDL (Cropland Data Layer)
- NASA POWER (weather)
- NRCS SSURGO (soil)

---

## ✅ Task Status

| Task                                    | Status      | Notes                               |
| --------------------------------------- | ----------- | ----------------------------------- |
| Download field boundaries (20 fields)   | ✅ Complete | Maumee watershed, all crops         |
| Download CDL crop data (2020-2023)      | ✅ Complete | 80 records (4 years × 20 fields)    |
| Download SSURGO soil data               | ✅ Complete | 124 soil records                    |
| Download NASA POWER weather (2020-2023) | ✅ Complete | 29,220 daily records                |
| Merge datasets using field_id           | ✅ Complete | Combined boundaries + CDL + soil    |
| Create interactive web map              | ✅ Complete | Colored by crop, tooltips with soil |

---

## 📁 Output Files

```
data/
├── fields/
│   └── ohio_maumee_20.geojson              # 20 field boundaries
├── soil/
│   └── ohio_maumee_20_soil.csv             # SSURGO data
├── weather/
│   └── ohio_maumee_20_2020_2023.csv        # Daily weather
├── cdl/
│   ├── CDL_2020_39.tif                     # Ohio CDL 2020
│   ├── CDL_2021_39.tif                     # Ohio CDL 2021
│   ├── CDL_2022_39.tif                     # Ohio CDL 2022
│   ├── CDL_2023_39.tif                     # Ohio CDL 2023
│   └── ohio_maumee_20_cdl.csv             # Crop classifications
└── assignment-02/
    ├── fields_with_crops.geojson            # Fields + CDL merged
    ├── fields_with_crops_soil.geojson      # Fields + CDL + soil merged
    ├── soil_EPSG4326.csv                   # Soil data (dominant per field)
    └── my_fields_map.html                  # Interactive map
```

---

## 🗺️ Map Features

- Fields colored by 2023 crop type
- Satellite & Street basemaps (toggleable)
- Hover tooltips: Field ID, Crop, Area, Soil series, pH, OM%, Drainage
- Click popups: Full crop history, complete soil profile
- Legend showing crop colors

---

## 📊 Data Summary

| Metric          | Value                                 |
| --------------- | ------------------------------------- |
| Fields          | 20                                    |
| Total Area      | ~306 acres                            |
| Crops (2023)    | Corn, Soybeans, Winter Wheat, Alfalfa |
| Years of Data   | 2020-2023                             |
| Weather Records | 29,220 (daily)                        |
| Soil Records    | 124 (multiple horizons per field)     |

---

## 🔄 Remaining Tasks

- [ ] Add weather data to merged dataset
- [ ] Add weather layer to web map
- [ ] Calculate Growing Degree Days (GDD)
- [ ] Analyze crop rotation patterns
- [ ] Create soil-crop suitability analysis

---

_Last updated: 2026-03-01_
