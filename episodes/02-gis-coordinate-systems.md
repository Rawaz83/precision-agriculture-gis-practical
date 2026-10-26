---
title: "Lecture 2: GIS Fundamentals and Coordinate Systems"
teaching: 40
exercises: 35
---

:::::::::::::::::::::::::::::::::::::::: questions

- How does a GIS store locations and their attributes?
- What is the difference between latitude and longitude?
- Why do EPSG:4326 and EPSG:32638 use different coordinate units?
- How can Google Earth Pro show decimal degrees and UTM coordinates?

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: objectives

By the end of this lesson, students should be able to:

1. Explain the role of geometry, attributes and coordinate reference systems in GIS.
2. Read latitude and longitude and convert degrees-minutes-seconds to decimal degrees.
3. Distinguish geographic coordinates from projected metre-based coordinates.
4. Identify WGS 84 (EPSG:4326) and WGS 84 / UTM Zone 38N (EPSG:32638).
5. Record two agricultural observations in Google Earth Pro and export a KMZ file.
6. Explain the difference between changing coordinate **display** and reprojecting GIS data.

::::::::::::::::::::::::::::::::::::::::

## 1. What does GIS store?

A Geographic Information System (GIS) links **where** something is (geometry) with **what** it is (attributes). A record also needs a coordinate reference system, or **CRS**, so software can interpret its numeric position correctly.

For example, one agricultural observation can contain:

| Element | Example |
|---|---|
| Geometry | Point |
| Latitude | 35.5600° N |
| Longitude | 45.4300° E |
| Attribute | Soil observation |
| CRS | WGS 84 / EPSG:4326 |

The coordinates above are **illustrative**, not survey measurements of a specific field.

A GIS may combine points (soil samples), lines (irrigation pipes), polygons (field boundaries) and rasters (satellite imagery or elevation).

## 2. Latitude and longitude

![Original educational diagram showing how latitude and longitude divide the Earth](https://upload.wikimedia.org/wikipedia/commons/6/62/Latitude_and_Longitude_of_the_Earth.svg)

*Figure 1. Latitude and longitude on Earth. Original illustration by [Djexplo on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Latitude_and_Longitude_of_the_Earth.svg), dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Unmodified.*

**Latitude** measures angular position north or south of the Equator (0° latitude). **Longitude** measures angular position east or west of the Prime Meridian (0° longitude).

- Geographic latitude ranges from -90° to +90°.
- Longitude is commonly represented between -180° and +180°.
- North and east values are positive in signed decimal-degree notation; south and west values are negative.

![Original globe diagram showing latitude and longitude angles used to locate a point](https://upload.wikimedia.org/wikipedia/commons/9/99/Earth_coordinates.svg)

*Figure 2. Latitude and longitude angles for one point on Earth's surface. Original diagram by Brews ohare, vector version by [CheChe on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Earth_coordinates.svg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Unmodified.*

### Exercise: Reading a position

An illustrative position near Sulaymaniyah is **35.5600° N, 45.4300° E**.

- Which number is latitude? **35.5600**
- Which number is longitude? **45.4300**
- In which hemispheres is the point? **Northern and Eastern**

:::::::::::::::::::::::::::::::::::::::: challenge

### Quick check: Coordinate order

A CSV has columns called \`longitude\` and \`latitude\`. When importing into QGIS as a point layer, which should be the X and Y fields?

:::::::::::::::::::::::: solution

### Answer

For this CSV, select **X = longitude** and **Y = latitude**, and set the source geographic CRS to **EPSG:4326**. Do not confuse the column order used in some web APIs with the X/Y fields in the QGIS importer.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 3. Decimal degrees and degrees-minutes-seconds

The same position can be expressed using different **formats**:

- Decimal degrees (DD): **35.5000° N**
- Degrees, minutes, seconds (DMS): **35° 30′ 00″ N**

Convert DMS to decimal degrees:

\`DD = degrees + minutes/60 + seconds/3600\`

For a south or west position, apply a negative sign to the absolute converted value.

:::::::::::::::::::::::::::::::::::::::: challenge

### Practice: DMS conversion

Convert **35° 30′ 00″ N** and **45° 26′ 00″ E** to decimal degrees.

:::::::::::::::::::::::: solution

### Worked answer

Latitude: 35 + 30/60 = **35.5000° N**.

Longitude: 45 + 26/60 = **45.4333° E** (rounded to four decimal places).

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 4. Geographic CRS versus projected CRS

A **geographic CRS** describes locations with angular coordinates such as latitude and longitude. WGS 84 geographic coordinates use **EPSG:4326**, with degrees as units.

A **projected CRS** represents the curved Earth on a flat coordinate plane. Many projected coordinate systems use metres for X and Y.

| Attribute | WGS 84 geographic | WGS 84 / UTM Zone 38N |
|---|---|---|
| EPSG code | **4326** | **32638** |
| Typical coordinates | Latitude, longitude | Easting, northing |
| Coordinate units | Degrees | Metres |
| Use in this course | Recording positions | Local field measurements and mapped analysis |

:::::::::::::::::::::::::::::::::::::::: callout

### Important: Assigning a CRS is not the same as reprojecting

**Assigning** a source CRS tells QGIS what the existing numbers mean. **Reprojecting** transforms those numbers into another CRS. Changing the **display format** in Google Earth Pro only changes how coordinates are shown; it does not mean the exported placemark has become a projected UTM dataset.

::::::::::::::::::::::::::::::::::::::::

### Watch: Coordinate reference systems in QGIS

The original video below demonstrates multiple GIS layers using different CRSs and how QGIS displays them together using on-the-fly reprojection.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/BRe1CpqziZk" title="QGIS for beginners: Coordinate Reference Systems with Gavin Fleming" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [QGIS for beginners: Coordinate Reference Systems with Gavin Fleming](https://www.youtube.com/watch?v=BRe1CpqziZk), QGIS official channel, 2022. Video hosted and owned by its YouTube creator.*

## 5. How UTM zones work

The Universal Transverse Mercator (UTM) system divides most of Earth's land areas into 60 longitudinal zones, typically **6 degrees** wide. Zones are numbered from west to east. Coordinates use a zone, hemisphere and metric **easting** and **northing**.

![Original Wikimedia Commons world map of Universal Transverse Mercator grid zones](https://upload.wikimedia.org/wikipedia/commons/b/b7/Universal_Transverse_Mercator_zones.svg)

*Figure 3. Original UTM zone world map by [cmglee, STyx, Wikialine and Goran tek-en on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Universal_Transverse_Mercator_zones.svg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Unmodified; irregular zones are highlighted in the original map.*

**Sulaymaniyah is in UTM Zone 38N.** The regular longitudinal span of Zone 38 is **42°E–48°E**, and its central meridian is **45°E**. A useful projected reference for many local agricultural mapping tasks is **EPSG:32638**.

:::::::::::::::::::::::::::::::::::::::: challenge

### Exercise: Choose the correct CRS

You have coordinates for a wheat-field boundary near Sulaymaniyah. You want to calculate its approximate area in square metres. Which is the more suitable choice for a local *planar* area calculation?

A. WGS 84 geographic, EPSG:4326  
B. WGS 84 / UTM Zone 38N, EPSG:32638

:::::::::::::::::::::::: solution

### Worked answer

**B**. EPSG:32638 uses metres and is well suited for many local mapping tasks near Sulaymaniyah. It is still important to check source accuracy and field digitization quality; no map projection eliminates those errors.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 6. Guided practical: Show DD and UTM in Google Earth Pro

**Software:** Google Earth Pro on Windows  
**Duration:** About 30–35 minutes  
**Study area:** Agricultural landscape near Sulaymaniyah

### Step 1 — Navigate to a field

1. Launch **Google Earth Pro**.
2. Search for \`Sulaymaniyah, Iraq\`.
3. Navigate to a visible agricultural area outside the urban centre.
4. Observe roads, fields and orchard blocks; select two illustrative observation locations.

### Step 2 — Set coordinate display to decimal degrees

1. Select **Tools → Options → 3D View**.
2. Under **Show Lat/Long**, choose **Decimal Degrees**.
3. Click **Apply** or **OK**.
4. Move the mouse over the map to observe the position display, or open a new placemark to inspect its location.

### Watch: Changing coordinate formats in Google Earth Pro

This YouTube walkthrough specifically covers latitude/longitude, UTM format and measurement-unit settings.

<iframe width="720" height="405" style="max-width:100%; border:0; aspect-ratio:16/9;" src="https://www.youtube-nocookie.com/embed/3ySwElnHlBY" title="Google Earth Pro: Change Coordinate Formats — Sabankou Kpatadoa" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

*Video: [Google Earth Pro: Change Coordinate System, DD, DMS, DMM and UTM](https://www.youtube.com/watch?v=3ySwElnHlBY), Sabankou Kpatadoa, 2023. Video hosted and owned by its YouTube creator.*

### Step 3 — Create two placemarks

1. Select **Add → Placemark**.
2. Move the placemark to your first observation position.
3. Name it \`Observation_A\` and record latitude and longitude.
4. Repeat for a second point named \`Observation_B\`.
5. Save the points in a folder named \`Lecture02_Coordinates\` in the Places panel.

### Step 4 — Inspect the UTM display

1. Reopen **Tools → Options → 3D View**.
2. Change **Show Lat/Long** to **Universal Transverse Mercator**.
3. For each placemark, inspect the displayed UTM zone, easting and northing.
4. Record the results in the following table.

| Observation | Latitude (°) | Longitude (°) | UTM zone | Easting (m) | Northing (m) |
|---|---|---|---|---|---|
| Observation_A | Student reading | Student reading | Student reading | Student reading | Student reading |
| Observation_B | Student reading | Student reading | Student reading | Student reading | Student reading |

### Step 5 — Export and verify

1. Right-click the folder \`Lecture02_Coordinates\`.
2. Choose **Save Place As** and export \`Lecture02_Coordinates.kmz\`.
3. Open that saved KMZ to confirm that both placemarks are present.
4. Keep your coordinate-recording table and a screenshot of both markers.

:::::::::::::::::::::::::::::::::::::::: caution

### Do not confuse display format with stored coordinates

KML/KMZ geographic positions are conventionally stored as **longitude, latitude** (and optional altitude) using WGS 84. Showing UTM in Google Earth does **not** change that internal geographic representation. The KMZ is a useful teaching file, not survey-certified land data.

::::::::::::::::::::::::::::::::::::::::

## 7. Optional QGIS comparison

If QGIS is already installed:

1. Create a new QGIS project.
2. Drag \`Lecture02_Coordinates.kmz\` into QGIS, choosing a suitable vector layer if prompted.
3. Inspect the point layer's CRS.
4. Set the **project CRS** to **EPSG:32638** and note how the coordinates shown in the QGIS status area change.
5. Explain why changing the project CRS does not automatically rewrite the original KMZ.
6. If asked to create projected data, use **Export → Save Features As** and select **EPSG:32638** for a new GeoPackage output.

## 8. Student assignment and rubric

Submit:

- \`Lecture02_Coordinates.kmz\` containing both named observation points.
- One screenshot of the two locations in Google Earth Pro.
- The completed decimal-degree and UTM coordinate table.
- A 100–150 word explanation comparing EPSG:4326 and EPSG:32638.
- A short note explaining image-based location uncertainty.

| Assessment criterion | Marks |
|---|---:|
| Two correctly saved locations | 2 |
| Correct decimal-degree readings | 2 |
| Correct UTM zone and coordinates | 2 |
| Verified KMZ and screenshot | 2 |
| CRS explanation and limitations | 2 |
| **Total** | **10** |

:::::::::::::::::::::::::::::::::::::::: challenge

### Reflection: Agricultural measurements

Why does it matter whether a field boundary comes from rough imagery interpretation or a surveyed GNSS boundary?

:::::::::::::::::::::::: solution

### Suggested explanation

A GIS can calculate an area from either, but the reliability of that number depends on the **quality of the boundary**, not just the CRS. Digitizing unclear image edges may introduce substantial error, whereas a well-designed survey can provide more defensible field measurements.

::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::

## 9. Sources and media credits

- [EPSG:4326 — WGS 84](https://epsg.io/4326).
- [EPSG:32638 — WGS 84 / UTM zone 38N](https://epsg.io/32638).
- [QGIS guidance on coordinate reference systems](https://docs.qgis.org/3.40/en/docs/gentle_gis_introduction/coordinate_reference_systems.html).
- [Google KML documentation](https://developers.google.com/kml/documentation/kmlreference).

All three illustrations above are **original works of their credited third-party creators** and have not been AI-generated or modified for this lesson. The first is CC0; the second and third are individually licensed CC BY-SA 4.0. Their respective image licenses remain in effect independently from the CC BY 4.0 license for the course's original text.

Both videos are embedded from their creators' YouTube channels, not copied or re-uploaded. YouTube videos are not assumed to be open-license material; if an embedded player is blocked, open its linked video page.

:::::::::::::::::::::::::::::::::::::::: keypoints

- **GIS = geometry + attributes + a valid CRS.**
- Latitude and longitude are angles, generally expressed in degrees.
- **EPSG:4326** is a geographic WGS 84 CRS.
- **EPSG:32638** is projected WGS 84 / UTM Zone 38N, useful for local metric mapping around Sulaymaniyah.
- Changing coordinate display formats is **not** reprojection.
- Save field observations with appropriate source, accuracy and CRS information.

::::::::::::::::::::::::::::::::::::::::
