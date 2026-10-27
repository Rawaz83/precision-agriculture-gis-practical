---
title: "Lecture 3: GPS, GNSS, and Agricultural Positioning"
teaching: 30
exercises: 30
---

:::::::::::::::::::::::::::::::::::::::: questions

- How can this lesson's technique support a mapped agricultural field observation?
- Which coordinate systems, measurement units and source files must be checked?
- What limitations would affect a real farm management decision?

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: objectives

By the end of this lecture, students should be able to:

- Explain GNSS errors, recognize uncorrected versus correction-enabled positioning, and import a latitude/longitude track.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

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

## 1A. Original visual examples and image interpretation

![Original image 1: The original NOAA illustration shows why GNSS observations depend on multiple satellites.](https://commons.wikimedia.org/wiki/Special:FilePath/GPS%20satellite%20constellation.jpg)

*Figure 1. The original NOAA illustration shows why GNSS observations depend on multiple satellites. Creator: [NOAA](https://commons.wikimedia.org/wiki/File:GPS_satellite_constellation.jpg). License: [Public domain](https://commons.wikimedia.org/wiki/Commons:Licensing). External original reproduced unchanged; not AI-generated.*

![Original image 2: This original equipment photograph shows a real agricultural DGPS reference-station system; no precision claim is inferred from the photograph.](https://commons.wikimedia.org/wiki/Special:FilePath/Claas%20Baseline%20HD.jpg)

*Figure 2. This original equipment photograph shows a real agricultural DGPS reference-station system; no precision claim is inferred from the photograph. Creator: [bdk](https://commons.wikimedia.org/wiki/File:Claas_Baseline_HD.jpg). License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## Interactive practical — Lecture 3

**[Open the interactive practice module for Lecture 3](files/course-interactives.html?lecture=3)**. It includes a topic-specific interactive calculation, the original images and videos credited in this lesson, four instant-feedback questions and browser-saved practice progress. Download the datasets and complete real GIS tasks in the relevant desktop application. All practice data are synthetic, and browser results are **not official university grades**.

## 2. Practical exercise — step by step

### Watch: Import and export CSV points in QGIS

Use this demonstration to map the lesson's synthetic GNSS points; it does not teach the full RTK correction process.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/jP-9kekpXYo" title="Import and export CSV points in QGIS" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Import and export CSV points in QGIS](https://www.youtube.com/watch?v=jP-9kekpXYo), by GIS & RS Made Easy. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


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

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download demo_gnss_observations.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_gnss_observations.csv)
- [Download synthetic_tractor_track.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_tractor_track.csv)

Import the tractor-track CSV as XY points in EPSG:4326. Sort records by `step` and compare positions over elapsed time. Import the original GNSS dataset separately, categorize by `quality_label`, and discuss why these labels are **illustrative**, not measured accuracy. Export the resulting layer to a GeoPackage and include it with the saved QGIS project.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

For the GNSS track CSV, compare the first and last recorded point. What would you have to measure in a real field before estimating path accuracy?

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

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


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
