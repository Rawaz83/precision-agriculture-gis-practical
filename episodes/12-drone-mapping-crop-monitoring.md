---
title: "Lecture 12: Drone Mapping and Crop Monitoring"
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

An orthomosaic joins corrected overlapping drone images into a georeferenced image. Ground sampling distance (GSD) describes ground pixel footprint; it does not equal position accuracy. Mapping quality also depends on GNSS, alignment, ground control, processing and terrain. This class does not require an actual drone flight.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS; optional permitted orthomosaic  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 2. Practical exercise — step by step

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

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
