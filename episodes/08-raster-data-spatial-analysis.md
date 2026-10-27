---
title: "Lecture 8: Raster Data and Spatial Analysis"
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

- Inspect raster cell size, CRS and NoData, and produce a slope map from a clearly synthetic elevation raster.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

::::::::::::::::::::::::::::::::::::::::

## 1. Principles

Rasters store values in cells. Cell size, extent, NoData, CRS and acquisition method determine what analyses are possible. A DEM represents terrain elevations; slope can be derived from it, but resolution and vertical accuracy must be appropriate to the intended farm decision.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS 3.x  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 1A. Original visual examples and image interpretation

![Original image 1: A historical QGIS raster-loading screenshot; the interface may differ from modern QGIS versions.](https://commons.wikimedia.org/wiki/Special:FilePath/QGis%20Data%20load%20-%2001%20raster%20topography.png)

*Figure 1. A historical QGIS raster-loading screenshot; the interface may differ from modern QGIS versions. Creator: [Yug and MissMJ](https://commons.wikimedia.org/wiki/File:QGis_Data_load_-_01_raster_topography.png). License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## Interactive practical — Lecture 8

**[Open the interactive practice module for Lecture 8](files/course-interactives.html?lecture=8)**. Work with synthetic course data, real externally sourced teaching images, a relevant YouTube walkthrough, a topic-specific calculation and four instant-feedback questions. Practice progress is stored only in your browser. Complete the real GIS work in QGIS or the software specified in this lesson; browser results are **not official university grades**.

## 2. Practical exercise — step by step

### Watch: Raster-band analysis and NDVI in QGIS

This is a complementary raster-calculator demonstration, not a DEM slope tutorial; focus on raster loading and cell alignment.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/t5EIb8AY7bU" title="Raster-band analysis and NDVI in QGIS" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Raster-band analysis and NDVI in QGIS](https://www.youtube.com/watch?v=t5EIb8AY7bU), by Burka GeoTech. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


1. Obtain a permitted sample georeferenced DEM and record its source.
2. Load the raster with Layer > Add Layer > Add Raster Layer.
3. In Layer Properties > Information, note CRS, dimensions, cell size, units and NoData.
4. Display the DEM with grayscale or pseudocolor symbology.
5. Run an available Processing Toolbox Slope algorithm and inspect its parameters.
6. Compare the DEM and slope layers and export a map with source attribution.


:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Can a 30-metre DEM reliably represent a narrow 20-centimetre-wide irrigation furrow?

:::::::::::::::::::::::: solution

### Answer and explanation

No. The feature is far below raster cell size; increased display sharpness cannot recover absent spatial detail.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download synthetic_elevation_utm38.asc](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_elevation_utm38.asc)
- [Download synthetic_training_field.geojson](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.geojson)

Open the **synthetic 40×40 ASCII elevation grid** as a raster. Assign its *source* CRS as EPSG:32638 if QGIS does not recognize it. Inspect extent, cell size (10 m), range of cell values and NoData settings. Use the Processing Toolbox to calculate a slope layer; note that this is an invented training surface and that slope results must **not** be interpreted as real terrain in Sulaymaniyah.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

Why is the 10-m cell size not evidence of real-world 10-m elevation accuracy?

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Raster metadata table, original DEM plus slope QGIS project, and interpreted map.

Use a descriptive filename beginning with Lecture08. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/raster_data.html)


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
