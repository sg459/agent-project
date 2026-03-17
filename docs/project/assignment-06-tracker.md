# Assignment-06-Tracker: Weather Analysis for Agricultural Fields

| Field          | Value                                           |
| -------------- | ----------------------------------------------- |
| **Assignment** | 06 — Weather Analysis for Agricultural Fields   |
| **Author**     | Ganbat ([@ganbat3](https://github.com/ganbat3)) |
| **Date**       | 2026-03-17                                      |
| **Status**     | **Completed**                                   |
| **Branch**     | `feature/assignment-6-weather` → `main`         |

---

## Summary

This assignment analyzes NASA POWER daily weather data for 20 Ohio Maumee watershed fields (2020–2023), calculates Growing Degree Days (GDD), characterizes seasonal climate patterns, and identifies weather anomalies compared to historical averages.

---

## Tasks Completed

### Data Loading & Preparation

| Task                                                                  | Status  | Notes                                               |
| --------------------------------------------------------------------- | ------- | --------------------------------------------------- |
| Load weather dataset from `data/weather/ohio_maumee_20_2020_2023.csv` | ✅ Done | 29,220 records, 20 fields                           |
| Ensure date column is in datetime format                              | ✅ Done | Used `pd.to_datetime()` with assertion verification |
| Handle missing fields/soil files gracefully                           | ✅ Done | Added `os.path.exists()` checks, files optional     |
| Fix CDL field_id parsing issues                                       | ✅ Done | Removed quotes/spaces from field_id values          |

### Data Filtering

| Task                                 | Status  | Notes                               |
| ------------------------------------ | ------- | ----------------------------------- |
| Filter to most recent growing season | ✅ Done | 2023 (May–September), 3,060 records |
| Create filtered dataset `weather_gs` | ✅ Done | Used for all downstream analysis    |

### Visualizations & Analysis

| Task                                               | Status  | Output                                                               |
| -------------------------------------------------- | ------- | -------------------------------------------------------------------- |
| Time-series: Daily temp (high/low) + precipitation | ✅ Done | `06_daily_temp_precip_timeseries.png`                                |
| Time-series by field                               | ✅ Done | `06_daily_temp_precip_by_field.png` (20 panels)                      |
| Rolling averages (7-day & 30-day)                  | ✅ Done | `06_rolling_averages_combined.png`, `06_rolling_averages_trends.png` |
| Anomaly detection vs historical                    | ✅ Done | Compared 2023 to 2020-2022 averages                                  |
| Dashboard assets                                   | ✅ Done | `output/dashboard_assets/`                                           |

---

## Key Findings: Most Significant Weather Trend

### ⚠️ Severe Drought in 2023 Growing Season

The most significant weather trend identified is a **severe drought** affecting all 20 fields throughout the entire 2023 growing season (May–September).

#### Precipitation Analysis

| Month     | Historical Avg (mm) | 2023 (mm) | % of Normal | Status             |
| --------- | ------------------- | --------- | ----------- | ------------------ |
| May       | 5,648               | 674       | **12%**     | 🔴 Extreme deficit |
| June      | 4,921               | 1,285     | **26%**     | 🔴 Severe deficit  |
| July      | 5,942               | 2,303     | **39%**     | 🔴 Severe deficit  |
| August    | 5,290               | 2,376     | **45%**     | 🔴 Severe deficit  |
| September | 4,359               | 663       | **15%**     | 🔴 Extreme deficit |

**Key statistic:** Every single month of the 2023 growing season had **less than 50%** of normal precipitation — a prolonged severe drought event.

#### Temperature Analysis

| Month     | Historical Avg (°C) | 2023 (°C) | Anomaly (°C) |
| --------- | ------------------- | --------- | ------------ |
| May       | 15.3                | 14.8      | -0.6         |
| June      | 21.7                | 20.1      | **-1.6**     |
| July      | 24.2                | 24.0      | -0.2         |
| August    | 23.8                | 22.2      | **-1.6**     |
| September | 19.2                | 19.7      | +0.4         |

The summer months (June, August) were **1.6°C cooler than historical averages**, compounding the drought stress on crops.

#### No Late-Season Frost

May minimum temperatures remained above 0°C (9.0°C average), so no late-season frost was detected.

---

## Data Quality & Missing Data Handling

### Weather Stations

- **Data source:** NASA POWER (daily weather data)
- **All 20 fields** had complete data coverage for 2020–2023
- **No missing weather stations** — all fields had continuous daily records

### Sentinel Values

- NASA POWER uses `-999` as a sentinel value for missing data
- **Action taken:** Replaced all `-999` values with `NaN` using pandas `.replace(-999.0, np.nan)`

### Missing Data Files

| File                                 | Status      | Handling                                         |
| ------------------------------------ | ----------- | ------------------------------------------------ |
| `data/fields/ohio_maumee_20.geojson` | Not present | Gracefully skipped with `os.path.exists()` check |
| `data/soil/ohio_maumee_20_soil.csv`  | Not present | Gracefully skipped with `os.path.exists()` check |

No interpolation or nearest-station substitution was required since all weather data was complete.

---

## Output Files Generated

### Main Notebook

- `notebooks/06_weather_analysis.ipynb` — Complete analysis with 39 cells

### Visualizations

```
notebooks/output/
├── 06_daily_temp_precip_timeseries.png
├── 06_daily_temp_precip_by_field.png
├── 06_rolling_averages_combined.png
├── 06_rolling_averages_trends.png
├── 06_precipitation_deficit_bars.png
├── 06_precipitation_pct_of_normal.png
├── 06_temperature_anomaly.png
└── 06_monthly_anomaly_comparison.csv

notebooks/output/dashboard_assets/
├── cumulative_precip_weather_trends.png
└── precip_gdd_weather_trends.png
```

---

## Validation

- ✅ Notebook JSON is valid
- ✅ All cells execute without errors
- ✅ All output files generated successfully
- ✅ Data quality checks passed

---

## Related Documentation

- Weather data: `data/weather/ohio_maumee_20_2020_2023.csv`
- CDL crop data: `data/cdl/ohio_maumee_20_cdl.csv`
- NASA POWER parameters: T2M, T2M_MAX, T2M_MIN, PRECTOTCORR, ALLSKY_SFC_SW_DWN, RH2M
