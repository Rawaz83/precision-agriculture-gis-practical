# Synthetic training CSV files

**These files are constructed illustrative data, not real observed soil, yield, drone or GNSS measurements. Do not apply them as fertilizer or operational prescriptions.**

Coordinate source CRS: WGS 84, EPSG:4326. Use X = longitude and Y = latitude when importing into QGIS.

- demo_soil_samples.csv: sample positions, artificial soil pH and a dimensionless nitrogen_index (not laboratory test results).
- demo_yield_points.csv: artificial yields in tonnes per hectare.
- demo_gnss_observations.csv: illustrative GNSS positions and conceptual environmental labels (not measured accuracy).
- demo_ndvi_pixels.csv: synthetic scaled red and near-infrared values for the NDVI calculation; one invalid zero-denominator row.

Coordinates are placed illustratively near Sulaymaniyah and do not describe an identified surveyed field.

Created for University of Sulaimani Precision Agriculture & GIS — Practical. License: CC BY 4.0 for these original synthetic training datasets.

## Regional modeled data (not synthetic, not field measured)

See [data/regional/README.md](regional/README.md) and the [interactive regional explorer](https://rawaz83.github.io/precision-agriculture-gis-practical/files/regional-data-lab.html). These tables derive from a lecturer-supplied NASA POWER-based MERRA-2 summary. Their model origin differs from the **fabricated** data above, but original upstream API retrieval metadata was not retained. The tables must **not** be represented as independently authenticated ground/station observations.
