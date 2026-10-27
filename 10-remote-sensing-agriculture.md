---
title: "Lecture 10: Remote Sensing for Agriculture"
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

- Assess a satellite scene using its bands, date, cloud cover and pixel dimensions, and explain scene interpretation limits.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

::::::::::::::::::::::::::::::::::::::::

## 1. Principles

Remote sensing collects information without direct contact. Spectral bands record radiation at different wavelengths, and satellite imagery differs in spatial, temporal, spectral and radiometric resolution. Cloud, shadows, seasonal crop stage and soil background influence interpretation.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS and satellite imagery browser  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 1A. Original visual examples and image interpretation

![Original image 1: Real Landsat false-colour imagery illustrates how vegetation and farm fields appear in multispectral imagery.](https://commons.wikimedia.org/wiki/Special:FilePath/Precision%20Farming%20in%20Minnesota%20-%20False%20Colour.jpg)

*Figure 1. Real Landsat false-colour imagery illustrates how vegetation and farm fields appear in multispectral imagery. Creator: [NASA Earth Observatory / Jesse Allen](https://commons.wikimedia.org/wiki/File:Precision_Farming_in_Minnesota_-_False_Colour.jpg). License: [Public domain](https://commons.wikimedia.org/wiki/Commons:Licensing). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## Interactive practical — Lecture 10

**[Open the interactive practice module for Lecture 10](files/course-interactives.html?lecture=10)**. Work with synthetic course data, real externally sourced teaching images, a relevant YouTube walkthrough, a topic-specific calculation and four instant-feedback questions. Practice progress is stored only in your browser. Complete the real GIS work in QGIS or the software specified in this lesson; browser results are **not official university grades**.

## 2. Practical exercise — step by step

### Watch: Sentinel-2 data search and NDVI processing in QGIS

Focus on locating imagery, viewing acquisition date, checking clouds and selecting compatible spectral bands.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/t5EIb8AY7bU" title="Sentinel-2 data search and NDVI processing in QGIS" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Sentinel-2 data search and NDVI processing in QGIS](https://www.youtube.com/watch?v=t5EIb8AY7bU), by Burka GeoTech. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


1. Open Copernicus Browser and navigate to an agricultural area near Sulaymaniyah.
2. Choose a crop-season date and inspect cloud coverage.
3. Identify satellite source, product type, acquisition date and pixel size.
4. Examine true-color and false-color displays if available.
5. Download a permitted georeferenced sample if possible, or document the browser visualization.
6. Identify two agricultural patterns and explain alternative reasons for each.


:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Do different colors on satellite imagery prove one field is diseased?

:::::::::::::::::::::::: solution

### Answer and explanation

No. Different crops, growth stage, soil, irrigation, atmospheric effects or image stretching can cause differences; verify with field evidence.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download synthetic_ndvi_grid.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_ndvi_grid.csv)

Use the official Copernicus Browser to inspect Sentinel-2 L2A scenes over an agricultural area near Sulaymaniyah. Record acquisition date, area of interest, platform, band names, cloud cover and pixel size. The optional CSV is a separate **fictional classroom array**; it is not satellite imagery.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

Why can comparing two dates from different crop-growth stages lead to wrong conclusions?

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Scene metadata, annotated screenshot and cautious interpretation paragraph.

Use a descriptive filename beginning with Lecture10. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://browser.dataspace.copernicus.eu/)
- [Reference 2](https://www.earthdata.nasa.gov/)


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
