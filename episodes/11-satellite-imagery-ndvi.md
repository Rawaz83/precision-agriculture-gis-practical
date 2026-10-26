---
title: "Lecture 11: Satellite Imagery and NDVI"
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

NDVI = (NIR − Red) / (NIR + Red), using comparable near-infrared and red reflectance values. NDVI is frequently between -1 and 1 but is not a direct measurement of disease, nitrogen requirement or crop yield. Clouds, soil background, zero denominators and acquisition date must be addressed.

:::::::::::::::::::::::::::::::::::::::: callout

### Course context

**University:** University of Sulaimani  
**Software:** Spreadsheet and optionally QGIS Raster Calculator  
**Study region:** Sulaymaniyah, Kurdistan Region of Iraq  
**Practice time:** Approximately 60 minutes

All supplied course CSV data are **synthetic educational examples**, not real field measurements.

::::::::::::::::::::::::::::::::::::::::

## 2. Practical exercise — step by step

1. Download the synthetic NDVI pixel CSV linked below.
2. Add an NDVI column to a spreadsheet.
3. For valid rows compute (nir - red) / (nir + red).
4. Mark denominator-zero rows as invalid instead of dividing by zero.
5. Compare vegetation, bare soil and water teaching examples.
6. Optionally use QGIS Raster Calculator on aligned red and NIR reflectance rasters.
7. Summarize two limitations of NDVI-based agricultural interpretation.

### Downloadable learning data

[NDVI practice CSV](https://raw.githubusercontent.com/Rawaz83/precision-agriculture-gis-practical/main/data/demo_ndvi_pixels.csv)

:::::::::::::::::::::::::::::::::::::::: challenge

### Knowledge check

Calculate NDVI for NIR 0.62 and Red 0.18.

:::::::::::::::::::::::: solution

### Answer and explanation

(0.62 − 0.18)/(0.62 + 0.18) = 0.44/0.80 = 0.55.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Student assignment

**Required submission:** Completed NDVI spreadsheet, optional map, and interpretation of two pixel values.

Use a descriptive filename beginning with Lecture11. Explain what the map or output shows, give its coordinate reference system and units when relevant, and mention at least one uncertainty.

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

- [Reference 1](https://www.earthdata.nasa.gov/)

:::::::::::::::::::::::::::::::::::::::: keypoints

- Document data origin, accuracy, CRS, units and dates.
- Check the validity of measurements, analyses and map exports.
- Treat synthetic examples as demonstrations only.
- Keep projects and supporting data together for reproducibility.

::::::::::::::::::::::::::::::::::::::::
