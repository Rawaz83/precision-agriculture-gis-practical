---
title: "Lecture 8: Raster Data and Spatial Analysis"
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

Rasters store values in cells. Cell size, extent, NoData, CRS and acquisition method determine what analyses are possible. A DEM represents terrain elevations; slope can be derived from it, but resolution and vertical accuracy must be appropriate to the intended farm decision.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** QGIS 3.x  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 2. Practical exercise — step by step

1. Obtain a permitted sample georeferenced DEM and record its source.
2. Load the raster with Layer > Add Layer > Add Raster Layer.
3. In Layer Properties > Information, note CRS, dimensions, cell size, units and NoData.
4. Display the DEM with grayscale or pseudocolor symbology.
5. Run an available Processing Toolbox Slope algorithm and inspect its parameters.
6. Compare the DEM and slope layers and export a map with source attribution.


:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Can a 30-metre DEM reliably represent a narrow 20-centimetre-wide irrigation furrow?

:::::::::::::::::::::::: solution

### Answer and explanation

No. The feature is far below raster cell size; increased display sharpness cannot recover absent spatial detail.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Raster metadata table, original DEM plus slope QGIS project, and interpreted map.

Use a descriptive filename beginning with Lecture08. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/raster_data.html)

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
