---
title: "Lecture 7: Vector Layers and Agricultural Mapping"
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

Vector layers represent point, line and polygon features with attributes. A polygon can store a field boundary and crop type; a line can store an irrigation route. For local planar area calculations use a suitable metric CRS, such as EPSG:32638 in Sulaymaniyah, rather than degree-squared coordinates.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS 3.x  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 2. Practical exercise — step by step

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

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
