# Assignment-03 Tracker — Exploratory Data Analysis

_Assignment: EDA on agricultural field summary data_
_Branch: feature/assignment-03-eda_
_Last updated: 2026-03-08_

---

## 📋 Task overview

**Goal:** Perform exploratory data analysis on `field_summary.csv` to understand variable distributions, relationships, and correlations across 20 Ohio Maumee watershed fields.

**Dataset:** `data/assignment-02/field_summary.csv`

**Variables analyzed:**

- **Numerical:** `organic_matter`, `ph`, `clay_pct`, `sand_pct`, `silt_pct`, `year`, `temp_avg`, `temp_max_avg`, `temp_min_avg`, `precip_total`, `solar_radiation`, `humidity`, `field_size_acres`
- **Categorical:** `crop`, `soil_name`, `soil_component`, `drainage_class`

---

## ✅ Task status

| Task                                          | Status      | Notes                                          |
| --------------------------------------------- | ----------- | ---------------------------------------------- |
| Distribution plot (organic matter)            | ✅ Complete | Histogram + KDE with mean/median lines         |
| Scatter plot (organic matter vs field size)   | ✅ Complete | With regression line overlay                   |
| Correlation heatmap (all numerical variables) | ✅ Complete | Lower-triangle masked, annotated               |
| Refine and save plots as high-res images      | ✅ Complete | Saved to `output/dashboard_assets/` at 300 DPI |
| Document EDA takeaways                        | ✅ Complete | See findings below                             |
| Log data cleaning steps                       | ✅ Complete | No additional cleaning required                |

---

## 📊 Key EDA findings

### Organic matter distribution

- **Mean:** 3.45%
- **Median:** 3.67%
- The distribution is **bimodal** (two distinct humps), suggesting two subpopulations of fields — one cluster with lower organic matter (~2–3%) and another with higher organic matter (~4.5–5%). The median is slightly higher than the mean, indicating a mild left skew overall.
- The bimodal shape may reflect different soil types, drainage conditions, or land management histories across the 20 fields.

### Correlation matrix highlights

| Variable pair                       | Correlation | Interpretation                                                                                   |
| ----------------------------------- | ----------: | ------------------------------------------------------------------------------------------------ |
| `clay_pct` vs `sand_pct`            |       -0.95 | Near-perfect inverse — expected since soil texture fractions sum to ~100%                        |
| `silt_pct` vs `sand_pct`            |       -0.95 | Same compositional constraint as above                                                           |
| `clay_pct` vs `silt_pct`            |        0.82 | Strong positive — clay-rich soils tend to also be silt-rich in this region                       |
| `temp_avg` vs `temp_min_avg`        |        0.73 | Strong positive — average temperature closely tracks daily minimums                              |
| `organic_matter` vs `clay_pct`      |        0.64 | Moderate positive — clay soils retain more organic matter                                        |
| `organic_matter` vs `ph`            |        0.58 | Moderate positive — higher OM fields tend to have higher pH in this dataset                      |
| `temp_max_avg` vs `temp_min_avg`    |       -0.61 | Moderate inverse — reflects diurnal temperature range; high max days do not always have high min |
| `solar_radiation` vs `temp_min_avg` |       -0.60 | Moderate inverse — high radiation days often have clearer skies and cooler nights                |
| `humidity` vs `precip_total`        |        0.53 | Moderate positive — wetter conditions correlate with higher humidity                             |
| `field_size_acres` vs all others    |  -0.15–0.12 | Weak — field size is largely independent of soil and weather variables                           |

### Data cleaning log

No additional data cleaning steps were required after reviewing the EDA outputs. No outliers warranting removal or transformation were identified in the organic matter distribution or correlation analysis. The data from the assignment-02 pipeline was already clean and analysis-ready.

---

## 📁 Output files

```text
output/dashboard_assets/
├── organic_matter_distribution.png    # Histogram + KDE (300 DPI)
└── correlation_heatmap.png            # Lower-triangle heatmap (300 DPI)
```

---

## 🔄 Remaining tasks

- [ ] Investigate the bimodal organic matter distribution — segment by `soil_name` or `drainage_class`
- [ ] Explore categorical variable relationships (crop type vs soil properties)
- [ ] Build predictive models using correlated variables

---

_Last updated: 2026-03-08_
