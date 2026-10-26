---
title: "Lecture 13: Management Zones and Variable-Rate Technology"
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

Management zones are hypotheses about areas with similar management needs. Multiple seasons, soils, yields and field checks are desirable. Variable-rate application needs agronomically justified rates, compatible equipment, calibration and monitoring. These synthetic records must NEVER be used as prescriptions.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS and spreadsheet  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 2. Practical exercise — step by step

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

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
