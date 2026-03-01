# PR: feat(skills): integrate borealBytes/ag-skills with Agent Skills IO format

## Summary

Import 12 agricultural data skills from borealBytes/ag-skills (branch: skills-content) into this repo using git subtree. Skills follow Agent Skills IO format and are auto-discoverable from `.skills/ag-skills/`.

## Changes

- **Git subtree**: Added `.skills/ag-skills/` from borealBytes/ag-skills (skills-content branch)
- **Attribution**: Created `THIRD_PARTY_NOTICES.md` with MIT license attribution to Boreal Bytes
- **Documentation**: Updated `.skills/ag-skills/README.md` with UV usage documentation
- **Agent integration**: Added skills-first section to `agentic/instructions.md` and updated hierarchy in `agentic/custom-instructions.md`

## Skills Imported

### Data Download (7)

| Skill               | Description                        |
| ------------------- | ---------------------------------- |
| field-boundaries    | USDA NASS Crop Sequence Boundaries |
| ssurgo-soil         | USDA NRCS SSURGO soil data         |
| nasa-power-weather  | NASA POWER weather data            |
| cdl-cropland        | USDA Cropland Data Layer           |
| sentinel2-imagery   | ESA Sentinel-2 satellite imagery   |
| landsat-imagery     | USGS Landsat satellite imagery     |
| interactive-web-map | Interactive web maps               |

### EDA/Analysis (5)

| Skill           | Description          |
| --------------- | -------------------- |
| eda-explore     | Data exploration     |
| eda-visualize   | Data visualization   |
| eda-correlate   | Correlation analysis |
| eda-time-series | Time series analysis |
| eda-compare     | Group comparisons    |

## Validation

- [x] Skills follow Agent Skills IO format (SKILL.md with YAML frontmatter)
- [x] MIT license attribution added to THIRD_PARTY_NOTICES.md
- [x] UV usage documented in .skills/ag-skills/README.md
- [x] Skills-first rule added to agentic/instructions.md
- [x] Skills added to hierarchy in agentic/custom-instructions.md

## Updating Skills

```bash
git subtree pull --prefix=.skills/ag-skills ag-skills skills-content --squash
```

---

**Status:** Ready for Review
**Branch:** skills-import
**Author:** Agent
