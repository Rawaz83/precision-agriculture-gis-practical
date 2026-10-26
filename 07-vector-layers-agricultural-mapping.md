---
title: "Lecture 7: Vector Layers and Agricultural Mapping"
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

- Digitize vector layers, record geometry attributes, and create a metric map and print layout.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

::::::::::::::::::::::::::::::::::::::::

## 1. Principles

Vector layers represent point, line and polygon features with attributes. A polygon can store a field boundary and crop type; a line can store an irrigation route. For local planar area calculations use a suitable metric CRS, such as EPSG:32638 in Sulaymaniyah, rather than degree-squared coordinates.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS 3.x  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 1A. Original visual examples and image interpretation

![Original image 1: The diagram highlights the distinctions among points, lines and polygons.](https://commons.wikimedia.org/wiki/Special:FilePath/Simple%20vector%20map.svg)

*Figure 1. The diagram highlights the distinctions among points, lines and polygons. Creator: [M. W. Toews](https://commons.wikimedia.org/wiki/File:Simple_vector_map.svg). License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). External original reproduced unchanged; not AI-generated.*

![Original image 2: The original QGIS layout screenshot shows how map outputs can be assembled for assessment.](https://commons.wikimedia.org/wiki/Special:FilePath/Print%20composer%20in%20QGIS.png)

*Figure 2. The original QGIS layout screenshot shows how map outputs can be assembled for assessment. Creator: [Path slopu](https://commons.wikimedia.org/wiki/File:Print_composer_in_QGIS.png). License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## 2. Practical exercise — step by step

### Watch: Digitizing polygons in QGIS

Follow the editing and vertex creation sequence. QGIS interface labels may differ by installation.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/6iF5yk-OrSw" title="Digitizing polygons in QGIS" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Digitizing polygons in QGIS](https://www.youtube.com/watch?v=6iF5yk-OrSw), by Terra Spatial. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


1. Load the soil points from Lecture 6 into a QGIS project.
2. Create a new GeoPackage polygon layer named farm_fields in EPSG:32638.
3. Digitize a training field polygon around the observation points.
4. Add text attributes field_id and crop.
5. Create a line layer representing a hypothetical irrigation route.
6. Calculate the polygon area in hectares from square metres divided by 10,000.
7. Create a print layout with title, legend and scale bar and export PDF.


:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Why cannot a planar area measured in squared degrees be directly reported in hectares?

:::::::::::::::::::::::: solution

### Answer and explanation

Degrees are angular units, not fixed metres. Reproject to a suitable metric CRS or use an appropriate geodesic area algorithm before converting to hectares.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download synthetic_training_field.geojson](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.geojson)
- [Download synthetic_training_field.kml](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.kml)

Import the GeoJSON with polygon, line and points. Duplicate it to a writable GeoPackage before editing; do not modify the original. In EPSG:32638, calculate metric area in hectares using square metres divided by 10,000. Create a layout PDF containing the polygon, route and point features with a legend and data disclaimer.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

Explain how the feature types relate to a field, irrigation path and sample positions.

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** GeoPackage, area attribute, and final map PDF with legend and units.

Use a descriptive filename beginning with Lecture07. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_vector/attribute_table.html)


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
