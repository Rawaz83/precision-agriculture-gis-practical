---
title: "Lecture 6: Introduction to QGIS"
teaching: 30
exercises: 30
---

:::::::::::::::::::::::::::::::::::::::: questions

- How can this lesson's technique support a mapped agricultural field observation?
- Which coordinate systems, measurement units and source files must be checked?
- What limitations would affect a real farm management decision?

::::::::::::::::::::::::::::::::::::::::


:::::::::::::::::::::::::::::::::::::::: callout

### Interactive GIS laboratory — guided practice

Before or after this lecture, open the **[Interactive Farm GIS Laboratory](files/interactive-lab.html)**. Explore the synthetic field, inspect layers, practise drawing a polygon, try an NDVI calculation, and complete the self-marking knowledge check. The activity is formative and is **not** an official grade.

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: objectives

By the end of this lecture, students should be able to:

- Locate QGIS panels, import source data with correct CRS, and save a portable GIS project with its layer files.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

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

## 1A. Original visual examples and image interpretation

![Original image 1: A real screenshot of QGIS demonstrates the Layers panel, map canvas and other basic desktop GIS elements, though menus can differ by software version.](https://commons.wikimedia.org/wiki/Special:FilePath/QGIS%20screenshot.webp)

*Figure 1. A real screenshot of QGIS demonstrates the Layers panel, map canvas and other basic desktop GIS elements, though menus can differ by software version. Creator: [Wikideas1](https://commons.wikimedia.org/wiki/File:QGIS_screenshot.webp). License: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## 2. Practical exercise — step by step

### Watch: Import/export CSV coordinates with QGIS

Watch the delimited text import and check the X/Y coordinate fields against the soil dataset.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/jP-9kekpXYo" title="Import/export CSV coordinates with QGIS" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Import/export CSV coordinates with QGIS](https://www.youtube.com/watch?v=jP-9kekpXYo), by GIS & RS Made Easy. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


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

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download demo_soil_samples.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_soil_samples.csv)
- [Download synthetic_training_field.geojson](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.geojson)

Add the soil points and GeoJSON farm layers to one QGIS project. Confirm point CRS EPSG:4326. Save a copy of the polygon in EPSG:32638 using Export > Save Features As and explain why reprojection alters stored numbers without moving geographic features. Reopen the `.qgz` file after closing QGIS.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

List the source CRS, project CRS and any exported target CRS separately. Why can all three differ?

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

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


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
