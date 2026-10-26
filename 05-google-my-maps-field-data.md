---
title: "Lecture 5: Google My Maps and Field Data"
teaching: 30
exercises: 30
---

:::::::::::::::::::::::::::::::::::::::: questions

- What agricultural problem does this technology address?
- What information and software are needed to use it responsibly?
- What evidence is required before making a field-management decision?

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: objectives

After this lecture students should be able to explain the topic, complete its practical workflow, preserve the source data and interpret its limitations.

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

## 2. Practical exercise — step by step

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

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
