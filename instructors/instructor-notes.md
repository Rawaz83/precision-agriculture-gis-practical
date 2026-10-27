---
title: 'Instructor Notes'
---

# Instructor notes: Precision Agriculture & GIS practical

## Interactive laboratory

Open [Interactive Farm GIS Laboratory](files/interactive-lab.html) alongside Lectures 1, 6, 7, 9 and 11.

**Suggested 60-minute class:**
1. First 10 min — students distinguish point, line, polygon and raster concepts.
2. Next 15 min — students toggle synthetic farm layers and inspect soil sample attributes.
3. Next 15 min — each student draws and downloads a new polygon and records its approximate area.
4. Next 10 min — students adjust red and NIR values and explain how NDVI changes.
5. Final 10 min — students complete the self-marking quiz (pass threshold 4/5) and submit a map screenshot plus a brief reflection using your institution's approved submission system.

## Data limitations

This laboratory uses **synthetic** GeoJSON, soil sample and tractor-track datasets. Field geometry is not surveyed; imagery background does not prove exact property boundaries or agronomic conditions. Approximate polygon areas use a spherical-Earth algorithm and are for educational comparison only. Do not use these data for real management, cadastral or scientific conclusions.

## Assessment policy and accessibility

Browser-stored progress and quiz marks are **not verified** and cannot serve as an official gradebook. Students may reset browser data. Accept alternative evidence (QGIS project, GeoJSON download, screenshot or explanation) if device restrictions prevent Leaflet, JavaScript, or OSM maps from loading. Provide an alternative offline GIS activity for students who cannot access the map.

Use the official course assignment rubric, not the practice quiz alone, to assess student performance.

## Further development

The interactive laboratory is a first pilot. Before formal adoption, test with student devices, low-bandwidth mobile connections, and relevant accessibility tools. Review external library CDN availability, OpenStreetMap tile policy, and accessibility of map drawing.


## Classroom acceptance check

Before each course offering, open the published [laboratory](files/interactive-lab.html)
in a student browser and verify that: the field map appears; layers can be
toggled; soil markers show their synthetic attributes; polygon drawing changes
the displayed area and exports GeoJSON; NDVI sliders update the formula;
the five-question quiz returns feedback; and local progress is retained after
a same-browser refresh. Repeat on at least one phone. If the map library or
OpenStreetMap tiles are unavailable, use a QGIS-based alternative.

The separate `02 Publish: Interactive GIS Laboratory` GitHub workflow restores
the standalone app to the `gh-pages` publishing branch after routine Workbench
builds, because Workbench does not automatically publish arbitrary standalone
HTML from its source `files/` directory.

## Lecture 6 (Phase 2): Interactive QGIS laboratory

Public student page: [Interactive QGIS Training](files/qgis-training-lab.html).
Source standalone HTML: files/qgis-training-lab.html on main.

### Teaching sequence (75–90 minutes)

1. 0–10 min: identify menu, toolbar, Browser, Layers, map canvas, status bar.
2. 10–20 min: download 4 practice datasets and create project folders.
3. 20–40 min: CSV import with X longitude, Y latitude, EPSG:4326; expect 12 features.
4. 40–55 min: import 1 polygon, 1 line, 5 observation points from separate GeoJSON.
5. 55–70 min: project CRS EPSG:32638; export the field to EPSG:32638 GeoPackage.
6. 70–80 min: save/reopen project including source files and screenshot evidence.
7. 80–90 min: six-question self-marking formative quiz and limitations discussion.

### Instructor verification and rubric

Check that the downloaded GIS files have 1 polygon, 1 line, and 5 point
features; soil CSV contains 12 rows. Confirm the exported GeoPackage CRS is
EPSG:32638 and the project reopens without missing-layer warnings.

10 marks: correct CSV XY/CRS import (2), vector counts (2), projected GeoPackage
(2), reproducible project (2), map and scientific limitations explanation (2).

All practice features and soil values are SYNTHETIC and cannot support
research findings or real farm management.

### Browser interactions and accessibility

The annotated real QGIS screenshot has textual alternative controls, so
students can identify components using a keyboard. Accept offline equivalent
work where remote images or JavaScript cannot load. The browser's progress
tracker is self-reported and unverified; it does not capture student identity
or submit work to Moodle or Google Classroom.

Acceptance test: inspect screenshot source links; check 6 component
explanations, download URLs, wrong/correct CSV and CRS feedback, quiz grading,
refresh persistence and practice report download on PC and mobile.

The existing 02 Publish workflow has been extended to republish both
the farm GIS and QGIS training HTML files on every successful site rebuild.

## Interactive modules for Lectures 3–5 and 7–14

[Open the course-wide interactive hub](files/course-interactives.html?lecture=3). This provides eleven practical simulations using synthetic GIS datasets. Students access each module using the link from its corresponding lecture. The original two interactive laboratories for introductory farm GIS and desktop QGIS remain available separately.

### Suggested use and formal assessment

In every module: read the full lesson, discuss image/video examples, download synthetic GIS data, complete the software-based practical, use the numerical concept calculator and answer the four-question formative quiz (3/4 pass). The browser records three self-reported milestones: file download, practical completion, and quiz pass. Records are stored in the student's current browser, and students may clear them. **They are not official academic grades or evidence that QGIS work occurred.** Require project files, maps, analysis logs and written discussion through the university's permitted submission route for formal grading.

### Topic-specific interpretation and safeguards

| Lecture | Interactive calculation/check | Limit |
|---|---|---|
| 3 | Geodesic point-to-point separation | Does not measure positioning accuracy |
| 4 | Rectangle area in hectares | Not a property survey |
| 5 | Longitude/latitude CSV X/Y assignment | Sharing and privacy must be checked separately |
| 7 | Square metres to hectares and feature geometry | Assumes trustworthy source area |
| 8 | Raster grid ground footprint | Spatial cell size is not measurement accuracy |
| 9 | Soil sample threshold count and pH arithmetic mean | No interpolation or soil recommendation |
| 10 | Illustrative cloud-free pixel count | Not a real satellite scene analysis |
| 11 | NDVI from red/NIR reflectance | Not a disease or fertilizer diagnosis |
| 12 | Simplified UAV ground-sampling distance | GSD is not horizontal mapping accuracy |
| 13 | Area × illustrative application rate | Not an operational rate prescription |
| 14 | GIS capstone deliverable checklist | Browser cannot verify the submitted data |

### Instructor quality checks

Open all 11 deep links in a desktop browser and confirm that each displays the matching topic, reference image and linked source, embedded video or YouTube fallback, correct download filenames and question set. Check units, negative and zero inputs, mathematical output, feedback for wrong and correct answers, and local progress saving/reloading. For low-bandwidth or accessibility needs, let students complete the equivalent text- and QGIS-based activity offline. External media retains third-party author/license terms as detailed in the lesson captions.

The Workbench publishing workflow now synchronizes all **three** standalone HTML apps into the generated `gh-pages` branch after successful course builds.

## Moodle and regional reanalysis resources

The `moodle/` directory contains a 65-question Moodle XML bank and 14 week-specific assignment/rubric briefs. These are **not installed in Moodle**: import into the lecturer's authenticated instance and create actual Assignment and Quiz activities separately. Public question-bank answers should be treated as formative preparation, never an undisclosed high-stakes test bank. Verify at least three imported questions across categories before assessment.

The [Northern Iraq regional viewer](files/regional-data-lab.html) uses 28 soil-wetness grid locations and 12 monthly modeled temperatures derived from user-supplied NASA POWER-based summaries. Original raw provider API responses were not included. Assign students a data-provenance check, grid-versus-ground classification, EPSG:4326 import, style of July/August values, and report limitations. Avoid claims about farm-level moisture, measured temperature or irrigation prescriptions.
