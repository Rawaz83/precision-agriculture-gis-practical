# Regionally grounded NASA POWER-derived teaching data

**Scientific classification:** MERRA-2 reanalysis/model-derived gridded data, not ground weather or soil measurements.

These two CSVs are cleaned subsets of the lecturer's pre-existing NASA POWER-derived
summary files. **The original NASA API responses and request logs were not retained
in the provided files. Therefore we have not independently authenticated each
numeric value against a fresh NASA download; treat them as teaching-derived source
products until checked.** Keep original synthetic data in `data/` distinct.

- `POWER_Sulaimani_2025_monthly_temperature_derived.csv`: 12 monthly
  mean 2-m air temperatures for the modeled location at latitude 35.5266,
  longitude 45.3195. Data were summarized from 8,760 hourly model values,
  UTC in 2025. Units °C. The supplied summary reports July 32.23 °C and
  August 32.60 °C. Not station measurements.
- `POWER_Northern_Iraq_2025_soil_wetness_derived.csv`: 28 gridded
  model-cell center coordinates for northern Iraq, July/August GWETTOP
  top-layer soil wetness fraction (0–1), historical 1984–2025 means,
  and difference/anomaly. **Relative saturation is not volumetric water content,
  not measured field moisture, and not a current irrigation recommendation.**
  The historical means include 2025, so the comparison is not independent.

## Official provider and reproducibility

- NASA POWER: https://power.larc.nasa.gov/
- Daily point API documentation: https://power.larc.nasa.gov/docs/services/api/temporal/daily/
- NASA POWER methods and data resolution: https://power.larc.nasa.gov/docs/methodology/

**Example new provider request (not claimed to recreate prior summary exactly):**

https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,PRECTOTCORR&community=AG&longitude=45.3195&latitude=35.5266&start=20250101&end=20251231&format=CSV

Reconstruct the regional GWETTOP summary only after verifying the
parameter is still available, its units, grid resolution, request
coordinates, time basis and archive product identifiers.

## GIS exercise (source CRS EPSG:4326)

1. Import soil wetness CSV through QGIS Delimited Text, setting X longitude,
   Y latitude, and EPSG:4326, or open the provided regional interactive viewer.
2. Symbolize GWETTOP July and August values separately; compare grid patterns.
3. Symbolize the July anomaly against a diverging legend centered on zero.
4. Import the 12-month air-temperature CSV as a nonspatial table; plot the
   monthly means, and explain warm-season climate conditions cautiously.
5. Document model grid resolution, units, archive date and uncertainties.
6. Submit QGIS .qgz, map PDF and a 200-word source/limitations assessment.

Citation: NASA POWER, NASA Langley Research Center (include product,
parameters, geographic coordinates, extraction date and access URL when
the original download metadata is available). Derived course tables
supplied by the lecturer. Reuse subject to original source terms.
