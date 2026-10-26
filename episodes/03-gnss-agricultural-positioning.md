---
title: "Lecture 3: GPS, GNSS, and Agricultural Positioning"
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

GNSS is the umbrella term for satellite navigation systems; GPS is one constellation. Position accuracy depends on signal geometry, sky visibility, reflections, equipment and any corrections. Ordinary phone positions are not equivalent to validated RTK survey data. The supplied CSV contains synthetic teaching coordinates, not measurements.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS 3.x and spreadsheet  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 2. Practical exercise — step by step

1. Download the synthetic GNSS CSV linked below.
2. Open QGIS and select Layer > Add Layer > Add Delimited Text Layer.
3. Select longitude as X, latitude as Y, with CRS EPSG:4326.
4. Open the points' attribute table and inspect the quality_label field.
5. Style point markers by quality_label and produce a screenshot.
6. Export the layer to GeoPackage and save the QGIS project.

### Downloadable learning data

[GNSS practice CSV](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_gnss_observations.csv)

:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Why could GNSS positions under trees vary between observations?

:::::::::::::::::::::::: solution

### Answer and explanation

Poor sky view, multipath reflections and satellite geometry can affect positions. Use open sky, repeat observations, and appropriate correction equipment when higher accuracy is required.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Categorized point map, GeoPackage, QGIS project, and comparison of phone GNSS versus RTK.

Use a descriptive filename beginning with Lecture03. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://www.gps.gov/systems/gnss/)

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
