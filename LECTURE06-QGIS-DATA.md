# Lecture 6 QGIS practice package

University of Sulaimani — Precision Agriculture & GIS — Practical (2026–2027).

**All features and soil values are SYNTHETIC TEACHING DATA. Never interpret as actual farm observations.**

Expected source layers:
- demo_soil_samples.csv: 12 sample locations, X longitude, Y latitude, EPSG:4326.
- qgis-training-field.geojson: 1 polygon feature.
- qgis-training-irrigation.geojson: 1 LineString feature.
- qgis-training-observations.geojson: 5 point features.

These files were separated from the prior mixed-geometry demonstration GeoJSON.
Coordinates are longitude/latitude in WGS 84 (EPSG:4326).
Use EPSG:32638 (WGS 84 / UTM zone 38N) when exporting a new
projected GeoPackage for local planar measurements in metres.
Changing the QGIS project CRS does not by itself reproject source data.

Recommended folder layout: Lecture06_QGIS/data, project, outputs.
Save L06_Agricultural_Map.qgz in project and field_utm38.gpkg in outputs.
Reopen the project and confirm that every layer resolves correctly.

Original synthetic course data, CC BY 4.0. No real measurements,
soil nutrient recommendations, legal land boundaries or operational maps.
