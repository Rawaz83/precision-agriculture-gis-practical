# Extra GIS practice package (synthetic)

These files are **constructed educational examples**, not actual surveyed
boundaries, soil results, crop imagery, drone flights or yield records. The
approximate positions near Sulaymaniyah are only chosen to make classroom
map imports plausible. They must NOT be used for navigation, property
boundaries, fertilizer recommendations or real farm operations.

| File | Format | Purpose | CRS / units |
|---|---|---|---|
| synthetic_training_field.geojson | GeoJSON | Polygon, irrigation line and five point observations | Longitude/latitude, WGS 84 |
| synthetic_training_field.kml | KML | Google Earth import for polygons, path and placemarks | KML WGS 84 longitude, latitude |
| synthetic_elevation_utm38.asc | ESRI ASCII raster | Teaching elevation grid for QGIS and raster operations | EPSG:32638 **must be assigned on import**, metres; elevation **arbitrary teaching metres** |
| synthetic_ndvi_grid.csv | CSV | Practice NDVI formula using reflectance-like values | Grid row/column identifiers, not georeferenced |
| synthetic_tractor_track.csv | CSV | Practice importing a GNSS-like sample track | EPSG:4326, latitude/longitude |

The ASCII DEM is a **formula-generated fictional terrain** of 40 by 40
cells (10 m grid), not a real digital elevation model. Because an ASCII grid
does not reliably store a projection, set its layer CRS to **EPSG:32638**
after loading it in QGIS (do not reproject arbitrary unreferenced coordinates).
Make sure students distinguish the ASCII grid's elevation units and projected
X/Y units from its fictional values.

## QGIS import tips

- GeoJSON: use Layer > Add Layer > Add Vector Layer.
- KML: open with Google Earth Pro or QGIS vector input.
- ASCII raster: Layer > Add Layer > Add Raster Layer, then verify the CRS.
- CSV: Add Delimited Text using **X longitude, Y latitude, source CRS EPSG:4326**.
- Keep project and data in the same workspace folder.
- The original course CSV datasets in this folder remain available separately.

Original teaching data created for the University of Sulaimani Precision
Agriculture & GIS — Practical course. **CC BY 4.0** with attribution.
