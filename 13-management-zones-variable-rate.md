---
title: "Lecture 13: Management Zones and Variable-Rate Technology"
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

- Sketch conceptual management zones from multiple datasets while explaining agronomic and machine requirements for VRT.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

::::::::::::::::::::::::::::::::::::::::

## 1. Principles

Management zones are hypotheses about areas with similar management needs. Multiple seasons, soils, yields and field checks are desirable. Variable-rate application needs agronomically justified rates, compatible equipment, calibration and monitoring. These synthetic records must NEVER be used as prescriptions.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS and spreadsheet  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 1A. Original visual examples and image interpretation

![Original image 1: A real zonation example based on measured pH, not a synthetic prescription.](https://commons.wikimedia.org/wiki/Special:FilePath/Soil%20improvements%20based%20on%20soil%20pH.jpg)

*Figure 1. A real zonation example based on measured pH, not a synthetic prescription. Creator: [Human & Physical Geography](https://commons.wikimedia.org/wiki/File:Soil_improvements_based_on_soil_pH.jpg). License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). External original reproduced unchanged; not AI-generated.*

![Original image 2: An original NDVI-based wheat-field illustration showing spatial variation, not a fertilizer-rate recommendation.](https://commons.wikimedia.org/wiki/Special:FilePath/Agricultural%20art.jpg)

*Figure 2. An original NDVI-based wheat-field illustration showing spatial variation, not a fertilizer-rate recommendation. Creator: [Antarsih](https://commons.wikimedia.org/wiki/File:Agricultural_art.jpg). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## 2. Practical exercise — step by step

### Watch: IDW mapping in QGIS as an input to management-zone assessment

A complementary workflow for visualizing variation; interpolation by itself does not establish variable-rate prescriptions.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/UCN0qR98BRs" title="IDW mapping in QGIS as an input to management-zone assessment" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [IDW mapping in QGIS as an input to management-zone assessment](https://www.youtube.com/watch?v=UCN0qR98BRs), by Sebastian Valdés Barraza. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


1. Import synthetic soil and yield CSV datasets as two QGIS point layers.
2. Style soil pH and yield values separately using graduated categories.
3. Compare their locations and patterns without asserting causal relationships.
4. Digitize two or three conceptual polygons into a new management_zones layer.
5. Add zone_id, evidence and confidence attributes.
6. Prepare a map labeled CONCEPTUAL ZONES ONLY – NOT AN APPLICATION PRESCRIPTION.
7. Describe what data and calibration would be required for real-world variable-rate applications.

### Downloadable learning data

[Soil CSV](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_soil_samples.csv) and [yield CSV](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_yield_points.csv)

:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Can one coincident high yield and high nitrogen-index value establish a fertilizer rate?

:::::::::::::::::::::::: solution

### Answer and explanation

No. A short synthetic dataset cannot determine response, cause or suitable rate. Local crop requirements, representative testing, agronomic calibration and operational validation are necessary.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download demo_soil_samples.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_soil_samples.csv)
- [Download demo_yield_points.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_yield_points.csv)
- [Download synthetic_training_field.geojson](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.geojson)

Import both point tables, map soil pH and yield separately, and compare broad spatial patterns. Create **conceptual** polygons inside the synthetic field boundary. Add a text attribute called `uncertainty` to every zone. A field controller cannot use this as a prescription: equipment format, agronomic calibration, approved rates and machine testing would all still be necessary.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

What evidence is missing before converting an illustrative zone map into a real fertilizer or seeding prescription?

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Conceptual zone GeoPackage, two thematic maps, and a VRT safeguards note.

Use a descriptive filename beginning with Lecture13. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://www.fao.org/)


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
