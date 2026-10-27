---
title: "Lecture 11: Satellite Imagery and NDVI"
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

- Compute NDVI, flag invalid pixels and explain why vegetation indices alone are not disease diagnoses.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

::::::::::::::::::::::::::::::::::::::::

## 1. Principles

NDVI = (NIR − Red) / (NIR + Red), using comparable near-infrared and red reflectance values. NDVI is frequently between -1 and 1 but is not a direct measurement of disease, nitrogen requirement or crop yield. Clouds, soil background, zero denominators and acquisition date must be addressed.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** Spreadsheet and optionally QGIS Raster Calculator  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 1A. Original visual examples and image interpretation

![Original image 1: NASA's vegetation-reflectance illustration clarifies the relationship between red and near-infrared signals.](https://commons.wikimedia.org/wiki/Special:FilePath/Ndvi%20example.jpg)

*Figure 1. NASA's vegetation-reflectance illustration clarifies the relationship between red and near-infrared signals. Creator: [NASA / Robert Simmon](https://commons.wikimedia.org/wiki/File:Ndvi_example.jpg). License: [Public domain](https://commons.wikimedia.org/wiki/Commons:Licensing). External original reproduced unchanged; not AI-generated.*

![Original image 2: A real QGIS example of a completed NDVI map.](https://commons.wikimedia.org/wiki/Special:FilePath/QGIS%20FinishedNDVIlayer.jpg)

*Figure 2. A real QGIS example of a completed NDVI map. Creator: [Felix Kullmann](https://commons.wikimedia.org/wiki/File:QGIS_FinishedNDVIlayer.jpg). License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## Interactive practical — Lecture 11

**[Open the interactive practice module for Lecture 11](files/course-interactives.html?lecture=11)**. Work with synthetic course data, real externally sourced teaching images, a relevant YouTube walkthrough, a topic-specific calculation and four instant-feedback questions. Practice progress is stored only in your browser. Complete the real GIS work in QGIS or the software specified in this lesson; browser results are **not official university grades**.

## 2. Practical exercise — step by step

### Watch: Sentinel-2 NDVI workflow in QGIS

Follow the real imagery-processing workflow after completing the synthetic arithmetic exercise.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/t5EIb8AY7bU" title="Sentinel-2 NDVI workflow in QGIS" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Sentinel-2 NDVI workflow in QGIS](https://www.youtube.com/watch?v=t5EIb8AY7bU), by Burka GeoTech. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


1. Download the synthetic NDVI pixel CSV linked below.
2. Add an NDVI column to a spreadsheet.
3. For valid rows compute (nir - red) / (nir + red).
4. Mark denominator-zero rows as invalid instead of dividing by zero.
5. Compare vegetation, bare soil and water teaching examples.
6. Optionally use QGIS Raster Calculator on aligned red and NIR reflectance rasters.
7. Summarize two limitations of NDVI-based agricultural interpretation.

### Downloadable learning data

[NDVI practice CSV](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_ndvi_pixels.csv)

:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Calculate NDVI for NIR 0.62 and Red 0.18.

:::::::::::::::::::::::: solution

### Answer and explanation

(0.62 − 0.18)/(0.62 + 0.18) = 0.44/0.80 = 0.55.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download demo_ndvi_pixels.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_ndvi_pixels.csv)
- [Download synthetic_ndvi_grid.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_ndvi_grid.csv)

Compute NDVI = (NIR − Red)/(NIR + Red) in a spreadsheet. For `nir=0.62` and `red=0.18`, check that NDVI is 0.55. Flag the row with zero denominator as invalid. Plot the 12×12 synthetic NDVI grid by row/column if desired, but do not georeference it: the rows and columns are **not** actual ground pixels.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

Why must satellite red and NIR bands have matched grid geometry and comparable reflectance scaling?

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Completed NDVI spreadsheet, optional map, and interpretation of two pixel values.

Use a descriptive filename beginning with Lecture11. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://www.earthdata.nasa.gov/)


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
