---
title: "Lecture 9: Soil Sampling and Fertility Mapping"
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

- Map soil pH observations, distinguish measured points from IDW surfaces, and recognize fertilizer-recommendation limitations.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

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

## 1A. Original visual examples and image interpretation

![Original image 1: An original agricultural soil-sampling photograph showing the physical work behind georeferenced sample points.](https://commons.wikimedia.org/wiki/Special:FilePath/Soil%20Sampling%20(48754451408).jpg)

*Figure 1. An original agricultural soil-sampling photograph showing the physical work behind georeferenced sample points. Creator: [United Soybean Board](https://commons.wikimedia.org/wiki/File:Soil_Sampling_(48754451408).jpg). License: [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/). External original reproduced unchanged; not AI-generated.*

![Original image 2: A real example of location-dependent soil-pH interpretation in an olive grove. It is not a map of our study area.](https://commons.wikimedia.org/wiki/Special:FilePath/Soil%20improvements%20based%20on%20soil%20pH.jpg)

*Figure 2. A real example of location-dependent soil-pH interpretation in an olive grove. It is not a map of our study area. Creator: [Human & Physical Geography](https://commons.wikimedia.org/wiki/File:Soil_improvements_based_on_soil_pH.jpg). License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## Interactive practical — Lecture 9

**[Open the interactive practice module for Lecture 9](files/course-interactives.html?lecture=9)**. Work with synthetic course data, real externally sourced teaching images, a relevant YouTube walkthrough, a topic-specific calculation and four instant-feedback questions. Practice progress is stored only in your browser. Complete the real GIS work in QGIS or the software specified in this lesson; browser results are **not official university grades**.

## 2. Practical exercise — step by step

### Watch: IDW interpolation in QGIS

Compare the workflow to the QGIS soil pH example. Interpolated cells are estimates, not new samples.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/UCN0qR98BRs" title="IDW interpolation in QGIS" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [IDW interpolation in QGIS](https://www.youtube.com/watch?v=UCN0qR98BRs), by Sebastian Valdés Barraza. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


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

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download demo_soil_samples.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_soil_samples.csv)
- [Download synthetic_training_field.geojson](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.geojson)

Use the soil observations to produce a graduated pH map. Keep source observation points visible when creating an optional IDW raster. Report number of samples, CRS, interpolation settings and limitations. The `nitrogen_index` is a dimensionless demonstration variable, **not** fertilizer kg/ha. Never calculate prescriptions from this file.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

Which two parts of the map are observations versus interpolated predictions?

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

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


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
