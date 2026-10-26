---
title: "Lecture 1: Introduction to Precision Agriculture"
teaching: 30
exercises: 30
---

:::::::::::::::::::::::::::::::::::::::::::: questions

- What is precision agriculture?
- Why is spatial variability important in farming?
- How can GPS, GIS, and satellite imagery support farm management?
- How can we create a basic digital farm map?

::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: callout

### Interactive GIS laboratory — guided practice

Before or after this lecture, open the **[Interactive Farm GIS Laboratory](files/interactive-lab.html)**. Explore the synthetic field, inspect layers, practise drawing a polygon, try an NDVI calculation, and complete the self-marking knowledge check. The activity is formative and is **not** an official grade.

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: objectives

By the end of this lecture, students will be able to:

1. Define precision agriculture and explain its objectives.
2. Identify common precision agriculture technologies.
3. Distinguish between points, lines, polygons, and raster data.
4. Locate an agricultural field using Google Earth Pro.
5. Create and export a digital farm boundary.
6. Explain how spatial information supports agricultural decisions.

::::::::::::::::::::::::::::::::::::::::::::

## 1. Introduction

Precision agriculture (PA) is a farm management approach that uses spatial, temporal, and other data to support management decisions.

Its purpose is to account for variability within agricultural fields and improve the efficiency of agricultural inputs and operations.

Traditional farming often applies uniform treatments across a field.

Precision agriculture allows farmers to make location-specific decisions based on measured conditions.

### Example: Fertilizer Application

Consider a wheat field in Sulaymaniyah.

Soil fertility may vary across the field:

- Zone A: Low nitrogen availability
- Zone B: Moderate nitrogen availability
- Zone C: High nitrogen availability

Applying the same fertilizer rate everywhere may be inefficient.

Using soil sampling, GPS, and GIS, the farmer can create a fertility map and develop different fertilizer recommendations for each zone.

:::::::::::::::::::::::::::::::::::::::::::: callout

### Key Concept

Precision agriculture does not simply mean using advanced machinery.

It means collecting relevant data, analyzing variability, making informed decisions, and evaluating the results.

::::::::::::::::::::::::::::::::::::::::::::

## 2. Important Precision Agriculture Technologies

| Technology | Agricultural Application |
|---|---|
| GPS/GNSS | Field positioning and machinery guidance |
| GIS | Agricultural mapping and spatial analysis |
| Remote sensing | Monitoring crop and land conditions |
| Satellite imagery | Vegetation and land-cover monitoring |
| Drones (UAVs) | High-resolution field observations |
| Soil sensors | Measuring soil conditions |
| Weather stations | Monitoring agricultural weather |
| Variable-rate technology | Adjusting agricultural inputs by location |


### Photo: GNSS guidance equipment

![A TeeJet Matrix 430 agricultural GNSS guidance display beside a GNSS antenna receiver](https://upload.wikimedia.org/wikipedia/commons/1/1c/Teejet_Matrix_430.jpg)

*Figure 1. A real agricultural GNSS guidance display and receiver. This is an example of positioning equipment, not a screenshot of a field map. Photograph: [Mr. Justice USA, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Teejet_Matrix_430.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Image reproduced unchanged.*

**Look closely:** Which component displays information to the tractor operator, and which component receives satellite navigation signals? How could knowing a tractor's location reduce missed passes or overlapping applications?

## 3. Understanding Spatial Data

GIS commonly uses vector and raster data.

### Vector Data

Vector data represents geographic objects using:

**Points**

Examples:
- Soil sampling locations
- Irrigation wells
- Weather stations

**Lines**

Examples:
- Irrigation pipelines
- Tractor routes
- Farm access roads

**Polygons**

Examples:
- Agricultural field boundaries
- Irrigation zones
- Soil management zones


### Visual guide: Points, lines, and polygons

![Original diagram of a simple GIS vector map identifying point wells, line rivers and a polygon lake](https://upload.wikimedia.org/wikipedia/commons/3/38/Simple_vector_map.svg)

*Figure 2. Vector data illustrated by wells (points), a river (line), and a lake (polygon). Illustration: [M. W. Toews, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Simple_vector_map.svg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Image reproduced unchanged.*

**Apply this to farming:** Replace the well with a soil-sampling location, the river with an irrigation pipe or tractor route, and the lake with a field boundary.

### Raster Data

Raster data consists of a grid of cells.

Examples:
- Satellite images
- NDVI maps
- Digital elevation models
- Temperature maps


### Visual guide: Vector versus raster representation

![Comparison of a continuous area represented by a precise vector polygon boundary and by raster grid cells](https://upload.wikimedia.org/wikipedia/commons/2/24/Area_in_spatial_raster_and_vector_data.svg)

*Figure 3. The same area represented by vector and raster models. Illustration: [Gegot, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Area_in_spatial_raster_and_vector_data.svg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Image reproduced unchanged.*

A **vector polygon** follows connected boundary vertices. A **raster** covers space with individual grid cells, so an edge is represented at the raster's cell resolution.

### Watch: Vector versus raster in GIS

This short video introduces points, lines, polygons, and raster grids. Watch before attempting Exercise 1.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/N-3zF10LbHg" title="Vector vs Raster Data in GIS — Felt" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Vector vs Raster Data in GIS: Key Differences for Mapping and Analysis](https://www.youtube.com/watch?v=N-3zF10LbHg), Felt (2024), via YouTube. Video remains hosted by its creator. If the embedded player is unavailable, use the linked YouTube page.*

:::::::::::::::::::::::::::::::::::::::::::: challenge

### Exercise 1: Identify the Data Type

Identify the most suitable GIS data representation for each feature:

1. An agricultural weather station
2. A tractor travel path
3. A wheat field boundary
4. A satellite-derived NDVI image

:::::::::::::::::::::::: solution

### Answers

1. Weather station: Point
2. Tractor path: Line
3. Wheat field boundary: Polygon
4. NDVI image: Raster

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::

## 4. Practical Activity: Digital Farm Mapping

**Software:** Google Earth Pro

**Study area:** Sulaymaniyah, Kurdistan Region of Iraq

**Estimated practical time:** 20 minutes

### Step 1: Open Google Earth Pro

1. Launch Google Earth Pro.
2. Enter "Sulaymaniyah, Iraq" into the search box.
3. Navigate toward an agricultural area.
4. Zoom in until agricultural field boundaries are visible.

### Step 2: Observe the Landscape

Identify at least three of the following features:

- Agricultural fields
- Roads
- Irrigation canals
- Orchards
- Buildings
- Water resources

Record your observations.


#### Watch before digitizing: Drawing a polygon in Google Earth Pro

This walkthrough shows how to create a polygon, edit its vertices, and correct an outline. It demonstrates the same type of polygon students will use for their training-field boundary.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/jAvZduECF0I" title="Google Earth Pro: How to Create and Edit Polygons — Sabankou Kpatadoa" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Google Earth Pro | How to Create and Edit Polygons](https://www.youtube.com/watch?v=jAvZduECF0I), Sabankou Kpatadoa (2023), via YouTube. Polygon creation begins at 0:13; editing begins around 3:46. Video remains hosted by its creator.*

### Step 3: Create a Farm Boundary

1. Select a visible agricultural field.
2. Click **Add > Polygon**.
3. Enter the name `Training Farm 01`.
4. Click around the boundary of the selected field.
5. Choose a suitable outline color.
6. Click OK to save the polygon.

### Step 4: Inspect the Boundary

1. Right-click your polygon.
2. Select Properties.
3. Open the Measurements tab.
4. Inspect the perimeter and area.
5. Record the area in hectares, if available.

### Step 5: Add a Point

1. Click **Add > Placemark**.
2. Place the marker on an identifiable feature.
3. Name the marker `Observation Point 01`.
4. Record its latitude and longitude.

### Step 6: Export the Data

1. Create a folder in the Places panel.
2. Move the farm polygon and observation point into it.
3. Right-click the folder.
4. Choose **Save Place As**.
5. Export it as a KMZ file.

Suggested filename:

`Lecture01_Farm_Observation.kmz`

:::::::::::::::::::::::::::::::::::::::::::: caution

### Important Note

The training field is selected for educational purposes.

Google Earth imagery is not necessarily current, and visually identified boundaries should not be treated as legally surveyed property boundaries.

::::::::::::::::::::::::::::::::::::::::::::

## 5. Guided Discussion

:::::::::::::::::::::::::::::::::::::::::::: challenge

### Exercise 2: Why Does Location Matter?

Two soil samples from the same agricultural field have different nitrogen concentrations.

**Question:** Why might a farmer use different fertilizer rates in these locations?

:::::::::::::::::::::::: solution

### Suggested Answer

Different soil nitrogen levels may indicate different fertilizer requirements.

The farmer can use georeferenced soil sampling results and GIS analysis to identify management zones.

However, fertilizer recommendations should also consider crop requirements, soil test interpretation, expected yield, and other relevant agronomic factors.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::: challenge

### Exercise 3: Choose the Appropriate Technology

Select the most appropriate technology for each task.

1. Measuring the position of a tractor
2. Producing a vegetation index from satellite imagery
3. Creating a digital soil sampling map
4. Automatically changing fertilizer application rates

:::::::::::::::::::::::: solution

### Suggested Answers

1. GNSS/GPS
2. Satellite remote sensing
3. GIS combined with georeferenced soil observations
4. Variable-rate application equipment and a prescription or control system

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::

## 6. Student Assignment

### Assignment Title

**Creating a Basic Agricultural Field Map**

Students must create a digital agricultural map using Google Earth Pro.

### Required Outputs

1. One agricultural field boundary polygon
2. At least two point markers
3. A screenshot showing the mapped features
4. A KMZ file containing the mapped features
5. A short written explanation of the map and its agricultural relevance

### Submission Filename

`Lecture01_StudentID.kmz`

### Assessment Rubric

| Assessment Criterion | Marks |
|---|---:|
| Correct field boundary | 3 |
| Two observation points | 2 |
| Correct KMZ export | 2 |
| Map screenshot | 1 |
| Agricultural explanation | 2 |
| **Total** | **10** |

Submit the files through the submission method specified by your lecturer.

## 7. Further Reading

- [QGIS Official Website](https://qgis.org/)
- [Google Earth](https://earth.google.com/)
- [NASA Earthdata](https://www.earthdata.nasa.gov/)
- [FAO Geospatial Information](https://www.fao.org/geospatial/)


## 8. Media attribution and reuse

The photographs and diagrams in this lesson are **original works by the credited external creators**, not AI-generated images. They are embedded from Wikimedia Commons without alteration. Their **CC BY-SA 4.0** licenses apply to each individual image, even though original written course content has a CC BY 4.0 license. See each caption for creator, source and license.

The videos are embedded from YouTube, attributed to their respective channels, and remain hosted on YouTube. Their presence in this lesson does not mean the videos are openly licensed for copying, redistribution or editing. Use the linked YouTube page if an embed is blocked by network or privacy settings.

:::::::::::::::::::::::::::::::::::::::::::: keypoints

- Precision agriculture uses data to support location-specific farm management.
- Agricultural fields may contain significant spatial variability.
- GPS/GNSS provides geographic positioning.
- GIS supports the storage, visualization, and analysis of spatial information.
- Points, lines, polygons, and rasters are fundamental GIS data structures.
- Google Earth Pro can create and export basic agricultural maps.
- KML and KMZ files can be used to exchange geographic features.

::::::::::::::::::::::::::::::::::::::::::::
