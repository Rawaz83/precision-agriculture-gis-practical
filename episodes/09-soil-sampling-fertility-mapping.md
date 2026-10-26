---
title: "Lecture 9: Soil Sampling and Fertility Mapping"
teaching: 30
exercises: 30
---

:::::::::::::::::::::::::::::::::::::::: questions

- What agricultural problem does this technology address?
- What information and software are needed to use it responsibly?
- What evidence is required before making a field-management decision?

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: objectives

After this lecture students should be able to explain the topic, complete its practical workflow, preserve the source data and interpret its limitations.

::::::::::::::::::::::::::::::::::::::::

## 1. Principles

Georeferenced sampling connects laboratory observations to field locations. Styling observed points is not the same as predicting between points. Interpolation uses assumptions that should be validated. The course's soil measurements are fictional, and nitrogen_index is not calibrated for fertilizer prescriptions.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS 3.x  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 2. Practical exercise — step by step

1. Import the synthetic soil CSV into QGIS using X longitude and Y latitude, EPSG:4326.
2. Symbolize observations using Graduated style by soil_ph.
3. Label a few sample_id values and inspect nitrogen_index.
4. Optionally run IDW interpolation for soil_ph using QGIS Processing.
5. Compare the modeled surface with the original observed points.
6. Export a map labeled SYNTHETIC TRAINING DATA – NOT FOR FARM RECOMMENDATIONS.

### Downloadable learning data

[Soil practice CSV](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_soil_samples.csv)

:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Why can an interpolation raster look detailed despite only twelve sample observations?

:::::::::::::::::::::::: solution

### Answer and explanation

Many rendered pixels are model estimates, not additional observations. Sampling density, method and uncertainty limit reliable interpretation.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** pH sample map, optional IDW raster, project and limitations paragraph.

Use a descriptive filename beginning with Lecture09. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

| Marking criterion | Marks |
|---|---:|
| Correct preparation of data, location and CRS | 2 |
| Practical workflow completed accurately | 3 |
| Clear map or specified output files | 2 |
| Agricultural interpretation and limitations | 2 |
| Organized, reproducible submission | 1 |
| **Total** | **10** |

:::::::::::::::::::::::::::::::::::::::: challenge

### Reflection

Describe one agricultural application of this technique in Sulaymaniyah. Which extra evidence or checking would be needed before applying the result on an actual farm?

:::::::::::::::::::::::: solution

### Suggested approach

Name the agricultural objective, describe the location-based information needed, and specify data quality, field validation and operational constraints. Avoid making real management recommendations from synthetic datasets.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 4. Further reading

- [Reference 1](https://www.fao.org/soils-portal/)

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
