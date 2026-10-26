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
