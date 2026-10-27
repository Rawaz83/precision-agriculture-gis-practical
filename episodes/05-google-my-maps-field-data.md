---
title: "Lecture 5: Google My Maps and Field Data"
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

- Import latitude/longitude CSV into Google My Maps, style by attribute, and check privacy before sharing.
- Prepare a reproducible practical exercise with named output files and documented uncertainty.

::::::::::::::::::::::::::::::::::::::::

## 1. Principles

Google My Maps can import a coordinate table, group features into layers, style them by attributes and share a map. Clear coordinate names, units and descriptions are essential. Public map sharing can expose sensitive real locations, so use synthetic or approved data in training.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** Google My Maps  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 1A. Original visual examples and image interpretation

![Original image 1: The agricultural parcels in this original drone photograph illustrate the geographic context in which students place My Maps observation markers.](https://commons.wikimedia.org/wiki/Special:FilePath/Aerial%20view%20of%20agricultural%20fields%20in%20Punjab%2C%20India.jpg)

*Figure 1. The agricultural parcels in this original drone photograph illustrate the geographic context in which students place My Maps observation markers. Creator: [Bhullargraphic](https://commons.wikimedia.org/wiki/File:Aerial_view_of_agricultural_fields_in_Punjab%2C_India.jpg). License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). External original reproduced unchanged; not AI-generated.*

**Observation task:** For each figure, explain which mapped property is actually observable and which agricultural decision would still require a field measurement.

## Interactive practical — Lecture 5

**[Open the interactive practice module for Lecture 5](files/course-interactives.html?lecture=5)**. It includes a topic-specific interactive calculation, the original images and videos credited in this lesson, four instant-feedback questions and browser-saved practice progress. Download the datasets and complete real GIS tasks in the relevant desktop application. All practice data are synthetic, and browser results are **not official university grades**.

## 2. Practical exercise — step by step

### Watch: Import a CSV into Google My Maps

Follow the import process, choosing latitude/longitude and `point_id` from the synthetic course table.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/kQPoN715YVc" title="Import a CSV into Google My Maps" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Import a CSV into Google My Maps](https://www.youtube.com/watch?v=kQPoN715YVc), by BM Tech Tutorials. Hosted by its creator on YouTube. If playback is blocked, follow the direct link. A video embed does not mean that the video is openly licensed for copying.*


1. Download the synthetic GNSS CSV linked below.
2. Visit Google My Maps, create a map and name it L05 Agricultural Observations.
3. Import the CSV into a new layer, selecting latitude and longitude as location fields.
4. Use point_id for the feature title and style by quality_label.
5. Inspect two marker descriptions and add a map-level note that data are synthetic.
6. Export as KML/KMZ if the available interface permits, and check privacy settings.

### Downloadable learning data

[GNSS practice CSV](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_gnss_observations.csv)

:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Why is it safer to label spreadsheet columns latitude and longitude rather than simply x and y?

:::::::::::::::::::::::: solution

### Answer and explanation

Explicit coordinate labels prevent import errors and help students recognize coordinate order and spatial reference.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 2A. Guided dataset extension

**Original, downloadable teaching datasets:**

- [Download demo_gnss_observations.csv](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_gnss_observations.csv)
- [Download synthetic_training_field.kml](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/synthetic_training_field.kml)

In Google My Maps, create one layer from the synthetic GNSS CSV and a second imported layer from the training KML. Confirm point titles are readable, set styles by `quality_label` and save a screenshot. Before sharing the result, inspect map permissions and state prominently that the mapped coordinates are fictional.

:::::::::::::::::::::::::::::::::::::::: challenge

### Data quality check

Why must the KMZ layer and imported point layer be compared visually even if they both use WGS 84 positions?

:::::::::::::::::::::::: solution

### Suggested answer guidance

A strong answer clearly distinguishes **synthetic teaching data** from measured agricultural observations, identifies the relevant software operations, records coordinate systems and units, and explains the uncertainty or validation needed. Compare your answer with the specific interpretation requirements of this lesson.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** My Maps screenshot, exported map if supported, and a short privacy statement.

Use a descriptive filename beginning with Lecture05. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://support.google.com/mymaps/)


## 5. Media source and copyright notes

Every image in this lecture is externally sourced from Wikimedia Commons; see the caption for its individual creator, original file page and license. Images have been linked unchanged and are not AI-generated. The course's original written text may use CC BY 4.0, but third-party images retain their individual licenses. YouTube videos remain hosted by their authors; no video file has been copied.

Original exercise CSVs, KML, GeoJSON and raster samples are constructed **synthetic educational data**. They are not measured field, crop or topographic records.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
