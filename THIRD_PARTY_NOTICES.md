# Third-Party Notices

This file contains attributions and license information for third-party components used in this project.

---

## borealBytes/ag-skills

| Field           | Value                                                                                |
| --------------- | ------------------------------------------------------------------------------------ |
| **Source**      | https://github.com/borealBytes/ag-skills                                             |
| **Branch**      | skills-content                                                                       |
| **License**     | MIT (as stated in upstream README)                                                   |
| **Description** | Agricultural data analysis skills for downloading and analyzing US agricultural data |

### Attribution

Skills authored by Boreal Bytes / Clayton Young ([@borealBytes](https://github.com/borealBytes)).

### Included Skills

**Data Download Skills:**

- `field-boundaries` - USDA NASS Crop Sequence Boundaries
- `ssurgo-soil` - USDA NRCS SSURGO soil data
- `nasa-power-weather` - NASA POWER weather data
- `cdl-cropland` - USDA NASS Cropland Data Layer
- `sentinel2-imagery` - ESA Sentinel-2 satellite imagery
- `landsat-imagery` - USGS Landsat satellite imagery
- `interactive-web-map` - Interactive web maps

**EDA/Analysis Skills:**

- `eda-explore` - Data exploration
- `eda-visualize` - Data visualization
- `eda-correlate` - Correlation analysis
- `eda-time-series` - Time series analysis
- `eda-compare` - Group comparisons

### License Text

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Updating Skills from Upstream

To pull the latest skills from the upstream repository:

```bash
git subtree pull --prefix=.skills/ag-skills ag-skills skills-content --squash
```

---

**Last updated:** 2026-03-01
