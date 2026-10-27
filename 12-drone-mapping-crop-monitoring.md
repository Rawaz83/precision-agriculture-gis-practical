---
title: "Lecture 12: Drone Mapping and Crop Monitoring"
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

- Distinguish raw drone imagery from georeferenced orthomosaics and explain GSD versus positional accuracy.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

::::::::::::::::::::::::::::::::::::::::

## 1. Principles

An orthomosaic joins corrected overlapping drone images into a georeferenced image. Ground sampling distance (GSD) describes ground pixel footprint; it does not equal position accuracy. Mapping quality also depends on GNSS, alignment, ground control, processing and terrain. This class does not require an actual drone flight.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS; optional permitted orthomosaic  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 1A. Original visual examples and image interpretation

![Original image 1: Real agricultural drone use in a field.](https://commons.wikimedia.org/wiki/Special:FilePath/Drone%20in%20Field%20(48743493743).jpg)

*Figure 1. Real agricultural drone use in a field. Creator: [United Soybean Board](https://commons.wikimedia.org/wiki/File:Drone_in_Field_(48743493743).jpg). License: [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/). External original reproduced unchanged; not AI-generated.*

![Original image 2: A real processed UAS-derived NDVI image illustrating high-resolution crop patterns, not a current survey.](https://commons.wikimedia.org/wiki/Special:FilePath/DroneMapper%20Processed%20NDVI%204cm%20GSD.png)

*Figure 2. A real processed UAS-derived NDVI image illustrating high-resolution crop patterns, not a current survey. Creator: [Stoermerjp](https://commons.wikimedia.org/wiki/File:DroneMapper_Processed_NDVI_4cm_GSD.png). License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## Interactive practical — Lecture 12

**[Open the interactive practice module for Lecture 12](files/course-interactives.html?lecture=12)**. It includes a subject-specific scenario calculator, credited real third-party images and videos, downloadable teaching data, four explanatory quiz questions and locally saved progress. Complete any required QGIS work in the desktop application. These synthetic exercises do **not** produce verified grades or operational farm recommendations.

## 2. Practical exercise — step by step

### Watch: Create final map layouts in QGIS

This video teaches presentation of orthomosaic-derived observations in QGIS, not drone flight planning or photogrammetry.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/ZnnRllsUXds" title="Create final map layouts in QGIS" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Create final map layouts in QGIS](https://www.youtube.com/watch?v=ZnnRllsUXds), by Descomplica QGIS. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


1. Obtain a permitted demonstration orthomosaic or other georeferenced sample imagery.
2. Load imagery into QGIS and inspect CRS, pixel size and data origin.
3. Create a scouting point GeoPackage with issue_type and notes attributes.
4. Digitize three observation points at visible surface features.
5. Categorize observations and prepare a map layout with scale and legend.
6. Write a ground verification plan, and identify local permissions required before any real flight.


:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

If orthomosaic ground pixel size is 3 cm, must its mapping accuracy be 3 cm?

:::::::::::::::::::::::: solution

### Answer and explanation

No. Pixel footprint is different from horizontal positional accuracy. Alignment, control points and GNSS quality all matter.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download synthetic_training_field.geojson](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.geojson)

Open the original photogrammetry tutorials from OpenDroneMap (linked below) and distinguish a raw drone image from a georeferenced orthomosaic. For a no-flight classroom task, place scouting points over the synthetic field polygon or an available properly licensed orthomosaic. Describe the observed *appearance* without inferring disease, nutrient status, or positional accuracy.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

Why does a 4-cm image pixel not guarantee a 4-cm horizontal positional accuracy?

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Scouting points GeoPackage, annotated orthomosaic map and safety/verification plan.

Use a descriptive filename beginning with Lecture12. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://www.opendronemap.org/)


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
