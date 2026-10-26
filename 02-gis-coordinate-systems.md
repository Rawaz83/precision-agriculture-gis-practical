---
title: "Lecture 2: GIS Fundamentals and Coordinate Systems"
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

A GIS combines spatial geometries, attributes and a coordinate reference system (CRS). Latitude and longitude in WGS 84 (EPSG:4326) are expressed in degrees. For metric mapping in Sulaymaniyah, WGS 84 / UTM zone 38N (EPSG:32638) is suitable for many local tasks; its coordinates are in metres. Reprojecting data is different from incorrectly assigning it a CRS.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** Google Earth Pro; QGIS optional  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 2. Practical exercise — step by step

1. Search for Sulaymaniyah in Google Earth Pro and zoom to an agricultural area.
2. In Tools > Options > 3D View, select decimal degree coordinates.
3. Add two placemarks and record their latitude and longitude.
4. Change the display to Universal Transverse Mercator and record zone, easting and northing.
5. Export both placemarks together as a KMZ.
6. Explain why geographical degrees should not be treated as metres.


:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Convert 35 degrees 30 minutes 00 seconds N into decimal degrees. Why is area measured in squared degrees not directly hectares?

:::::::::::::::::::::::: solution

### Answer and explanation

35.5000 degrees N. Degrees are angular units; use an appropriate projected metric CRS or geodesic area calculation for real ground area.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Two-point KMZ, coordinates table, screenshot, and 100-word CRS explanation.

Use a descriptive filename beginning with Lecture02. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://epsg.io/32638)
- [Reference 2](https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/coordinate_reference_systems.html)

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
