# Assignment-04 Tracker — Field Mapping

_Assignment: Geospatial mapping of agricultural fields with soil overlay_
_Branch: feature/assignment-04-mapping_
_Last updated: 2026-03-08_

---

## 📋 Task overview

**Goal:** Build a layered geospatial map of 20 Ohio Maumee watershed fields, overlay dominant soil type from SSURGO data, and produce both an interactive dashboard map (Folium HTML) and a static publication-quality image (matplotlib + contextily PNG).

---

## 📊 Spatial datasets combined

| Dataset          | File                                 | Format        | CRS                |                                Records | Join key         |
| ---------------- | ------------------------------------ | ------------- | ------------------ | -------------------------------------: | ---------------- |
| Field boundaries | `data/fields/ohio_maumee_20.geojson` | GeoJSON       | EPSG:4326 (WGS 84) |                            20 polygons | `field_id` (str) |
| Soil properties  | `data/soil/ohio_maumee_20_soil.csv`  | CSV (tabular) | N/A — no geometry  | 124 rows (multiple horizons per field) | `field_id` (int) |

### Merge strategy

The soil CSV contains multiple soil components and horizons per field. To produce a single dominant soil type per field, we sorted by `comppct_r` (component percentage) descending and retained only the first record per `field_id`. The resulting dominant soil table (20 rows) was merged onto the field GeoDataFrame via a left join on `field_id`.

---

## ✅ Task status

| Task                                         | Status      | Notes                                                          |
| -------------------------------------------- | ----------- | -------------------------------------------------------------- |
| Import field boundaries and soil data        | ✅ Complete | Force-added past `.gitignore` with `git add -f`                |
| Verify CRS alignment                         | ✅ Complete | No mismatch — soil CSV is tabular, inherits field CRS on merge |
| Plot field boundaries (base layer)           | ✅ Complete | matplotlib static plot                                         |
| Overlay dominant soil type with color coding | ✅ Complete | 11 distinct soil types across 20 fields                        |
| Build interactive Folium map                 | ✅ Complete | Tooltips, legend, satellite/street basemap toggle              |
| Build static PNG with basemap (contextily)   | ✅ Complete | Centroid markers on CartoDB Positron tiles, 300 DPI            |
| Create assignment-04 notebook                | ✅ Complete | `notebooks/04_field_mapping.ipynb`                             |

---

## ⚠️ Data alignment and CRS notes

### CRS projection

No CRS alignment issues were encountered. The field boundaries GeoJSON uses EPSG:4326 (WGS 84), and the soil data is a plain CSV with no spatial component — it joins to fields via `field_id`. On merge, the resulting GeoDataFrame retains EPSG:4326 from the field layer.

For the contextily basemap PNG, we reprojected to EPSG:3857 (Web Mercator) using `.to_crs(epsg=3857)` to align with basemap tile coordinates. This reprojection was straightforward with no data loss.

### Data type mismatch on merge

The `field_id` column was stored as `str` in the GeoJSON but `int64` in the soil CSV. This caused a `ValueError` on the initial merge attempt. The fix was casting the soil `field_id` to string with `.astype(str)` before merging.

---

## 🔍 Challenges — visualizing small field boundaries

The primary challenge in this assignment was **field polygon visibility at the watershed scale**. The 20 fields are individual farm parcels (ranging from ~0.001 to ~0.009 degrees in width) spread across approximately 1.6 degrees of longitude. At the zoom level required to show all fields on one map, the polygons render as tiny dots — too small to distinguish colors or shapes.

### Approaches attempted

| Approach                                  | Result                                                                                                     |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Direct polygon plot** (matplotlib)      | Fields appeared as small black dots; soil colors invisible                                                 |
| **Buffered polygons** (`.buffer(0.015)`)  | Colors visible, but field shapes distorted into circles and nearby fields overlapped — visually misleading |
| **Actual polygons + contextily basemap**  | Basemap added geographic context, but fields still too small to see colors against tile detail             |
| **Centroid markers + contextily basemap** | Clear, color-coded dots at each field location with basemap context — honest and readable                  |
| **Interactive Folium map**                | Best solution — users can zoom into individual fields to see actual shapes, colors, and tooltips           |

### Resolution

We adopted a **two-output strategy**:

1. **Interactive HTML (Folium)** — the primary dashboard view. Zoomable map with actual field polygons, hover tooltips (field ID, crop, area, soil type, drainage class), satellite/street basemap toggle, and a fixed legend. Saved as `output/dashboard_assets/fields_soil_map.html`.
2. **Static PNG (contextily + centroid markers)** — for reports, slides, and print. Uses colored point markers at field centroids on a CartoDB Positron basemap. Does not distort field geometry. Saved as `output/dashboard_assets/fields_soil_map.png` at 300 DPI.

---

## 📁 Output files

```text
notebooks/
└── 04_field_mapping.ipynb                     # Assignment notebook

output/dashboard_assets/
├── fields_soil_map.html                       # Interactive Folium map
└── fields_soil_map.png                        # Static map with basemap (300 DPI)
```

---

## 🔄 Remaining tasks

- [ ] Add crop type as a second overlay layer (toggle between soil and crop views)
- [ ] Add field labels on the Folium map (popup with full soil profile)
- [ ] Explore choropleth by organic matter or pH values
- [ ] Integrate weather data overlay (precipitation, temperature)

---

_Last updated: 2026-03-08_
