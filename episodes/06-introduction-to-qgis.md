---
title: "Lecture 6: Introduction to QGIS"
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

QGIS is an open-source spatial analysis program. A .qgz project generally stores layer references, styles and layouts, not necessarily the datasets themselves. GeoPackage can store spatial layers. A CSV with latitudes and longitudes must be imported with its correct CRS.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS 3.x  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 2. Practical exercise — step by step

1. Create folders data, project and outputs in a Lecture06 workspace.
2. Download the synthetic soil CSV linked below into data.
3. In QGIS find the Layers, Browser, Map Canvas and Processing panels.
4. Add the CSV using Delimited Text, X longitude, Y latitude, CRS EPSG:4326.
5. Open the attribute table to inspect soil_ph and nitrogen_index.
6. Export the layer to a GeoPackage and save project/L06.qgz.
7. Reopen the saved project and confirm that the layer paths work.

### Downloadable learning data

[Soil practice CSV](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_soil_samples.csv)

:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Why might a QGIS project show a missing-layer warning after copying only its .qgz file?

:::::::::::::::::::::::: solution

### Answer and explanation

The project references source files that were not copied or whose paths changed. Reconnect the layers or move the project with its source data.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Working QGIS project, GeoPackage, screenshot, and explanation of source files versus projects.

Use a descriptive filename beginning with Lecture06. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://docs.qgis.org/3.40/en/docs/training_manual/)

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
