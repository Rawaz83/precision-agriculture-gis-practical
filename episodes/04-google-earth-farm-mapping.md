---
title: "Lecture 4: Google Earth Pro for Farm Mapping"
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

A point denotes a place, a line a path, and a polygon an area. KML stores geographic features; KMZ packages KML with related resources. Image-digitized farm boundaries are approximate: imagery date, unclear field edges, placement and digitizing decisions all influence accuracy. They are not legal surveys.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** Google Earth Pro  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 2. Practical exercise — step by step

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

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
