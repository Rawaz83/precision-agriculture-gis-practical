---
title: "Lecture 4: Google Earth Pro for Farm Mapping"
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

- Identify points, lines and field polygons, produce a KMZ from a training field, and discuss imagery digitizing uncertainty.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

::::::::::::::::::::::::::::::::::::::::

## 1. Principles

A point denotes a place, a line a path, and a polygon an area. KML stores geographic features; KMZ packages KML with related resources. Image-digitized farm boundaries are approximate: imagery date, unclear field edges, placement and digitizing decisions all influence accuracy. They are not legal surveys.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** Google Earth Pro  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 1A. Original visual examples and image interpretation

![Original image 1: A real agricultural aerial photograph demonstrates how field edges, access roads and land-cover patches can be identified, but not legally surveyed.](https://commons.wikimedia.org/wiki/Special:FilePath/Aerial%20view%20of%20agricultural%20fields%20in%20Punjab%2C%20India.jpg)

*Figure 1. A real agricultural aerial photograph demonstrates how field edges, access roads and land-cover patches can be identified, but not legally surveyed. Creator: [Bhullargraphic](https://commons.wikimedia.org/wiki/File:Aerial_view_of_agricultural_fields_in_Punjab%2C_India.jpg). License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## Interactive practical — Lecture 4

**[Open the interactive practice module for Lecture 4](files/course-interactives.html?lecture=4)**. It includes a topic-specific interactive calculation, the original images and videos credited in this lesson, four instant-feedback questions and browser-saved practice progress. Download the datasets and complete real GIS tasks in the relevant desktop application. All practice data are synthetic, and browser results are **not official university grades**.

## 2. Practical exercise — step by step

### Watch: Google Earth Pro: create and edit polygons

Follow the polygon creation and editing demonstration before tracing the course's training boundary.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/jAvZduECF0I" title="Google Earth Pro: create and edit polygons" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Google Earth Pro: create and edit polygons](https://www.youtube.com/watch?v=jAvZduECF0I), by Sabankou Kpatadoa. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


1. Navigate to a cultivated area near Sulaymaniyah.
2. Make a folder called Lecture04_Farm in Google Earth Pro Places.
3. Use Add > Polygon to digitize one training field and name it Field_A.
4. Use Add > Path for a track and Add > Placemark for an observation.
5. Inspect the polygon's approximate area and perimeter under Properties > Measurements.
6. Save the complete folder as Lecture04_Farm.kmz and reopen it to verify.


:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Two students obtain different areas for the same field. Does that prove that the field changed?

:::::::::::::::::::::::: solution

### Answer and explanation

No. They may have traced different edges or used different imagery; assess positional and digitizing uncertainty before making that claim.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download synthetic_training_field.kml](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.kml)
- [Download synthetic_training_field.geojson](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.geojson)

Open the supplied KML in Google Earth Pro and compare its three geometry types: polygon boundary, irrigation line and observation placemarks. Make a copy of the folder and use Properties to adjust the polygon vertices without changing the provided original. Save your modified work as a new KMZ; then import the GeoJSON in QGIS and compare the feature counts.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

Does changing polygon shape alter calculated area? Record the measurement units and explain why neither shape is a cadastral survey.

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** KMZ with a polygon, path and placemark; screenshot; approximate area and three uncertainties.

Use a descriptive filename beginning with Lecture04. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://developers.google.com/kml/documentation/kml_tut)


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
