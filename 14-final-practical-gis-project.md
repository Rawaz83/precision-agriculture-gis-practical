---
title: "Lecture 14: Final Practical GIS Project"
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

- Prepare reproducible data, GIS analysis, a professional print map and a transparent short methods report.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

::::::::::::::::::::::::::::::::::::::::

## 1. Principles

The final project should answer a modest, explicit agricultural question through a reproducible GIS workflow. Distinguish observed from synthetic or modeled information. Results need an identifiable source, CRS, scale, analysis method, limitations and data attribution.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS and optional Google Earth Pro  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 1A. Original visual examples and image interpretation

![Original image 1: Example of preparing a QGIS print layout.](https://commons.wikimedia.org/wiki/Special:FilePath/Print%20composer%20in%20QGIS.png)

*Figure 1. Example of preparing a QGIS print layout. Creator: [Path slopu](https://commons.wikimedia.org/wiki/File:Print_composer_in_QGIS.png). License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). External original reproduced unchanged; not AI-generated.*

![Original image 2: Example GIS desktop map screen, useful for reviewing how a project is organized.](https://commons.wikimedia.org/wiki/Special:FilePath/QGIS%20screenshot.webp)

*Figure 2. Example GIS desktop map screen, useful for reviewing how a project is organized. Creator: [Wikideas1](https://commons.wikimedia.org/wiki/File:QGIS_screenshot.webp). License: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## 2. Practical exercise — step by step

### Watch: QGIS Print Layout complete guide

Use the relevant chapters to prepare a title, map, legend, north arrow and export a PDF.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/ZnnRllsUXds" title="QGIS Print Layout complete guide" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [QGIS Print Layout complete guide](https://www.youtube.com/watch?v=ZnnRllsUXds), by Descomplica QGIS. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


1. Choose one agricultural mapping question and write a one-sentence objective.
2. Create structured data, project, outputs and documentation folders.
3. Use at least two geographic layers including a point layer and a polygon or raster.
4. Record source, license, coordinate reference system and dates for each input.
5. Carry out a suitable spatial operation: area, buffer, thematic comparison or carefully labeled interpolation.
6. Export one readable final map PDF with legend, scale, title and attribution.
7. Prepare a 300–500-word report covering purpose, methods, results and limitations.
8. Reopen the project from the submission folder to test reproducibility.


:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

How should a student describe a result based solely on synthetic demonstration data?

:::::::::::::::::::::::: solution

### Answer and explanation

Clearly label it a teaching demonstration and refrain from asserting real field yield, nutrient levels, or management benefits.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download synthetic_training_field.geojson](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.geojson)
- [Download synthetic_elevation_utm38.asc](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_elevation_utm38.asc)
- [Download demo_soil_samples.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_soil_samples.csv)

Choose two synthetic layers with different geometry types. Produce a single project folder containing both source data and the `.qgz` file, a well-labeled final PDF, a short methods report, and a data-source inventory. Reopen the project from a copied folder as a reproducibility check. Document each external image or layer's original owner and reuse terms.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

What would a second student need to reproduce your exported map without contacting you?

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Complete QGIS project and its inputs, final PDF map, 300–500-word report and source inventory.

Use a descriptive filename beginning with Lecture14. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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
