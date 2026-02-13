# GmE 221 - Laboratory Exercise 2

## Overview
This laboratory performs a parcel-landuse overlay analysis using Python (GeoPandas).
Spatial data are retrieved from PostGIS using minimal SQL.
Overlay, area computation, percentage calculation, and classification are executed in Python.
The final output is exported as GeoJSON file for visualization in QGIS.

---

## Environment Setup
- Python 3.x
- PostgreSQL with PostGIS
- GeoPandas, SQLAlchemy, psycopg2

---

## How to Run
1. Activate the virtual environment
2. Run 'analysis.py' to execute the overlay and classification
3. Load the geenerated GeoJSON file in QGIS

---

## Output
- GeoJSON file: 'output/dominant_residential.geojson'
- Visualization in QGIS

## Reflection -- Interpreting GIS IO in Practice
- The difference between storing geometry in PostGIS is that this ----- stores the data while GeoPandas represents the data.
- This is considered as input because no analysis has been done. The idea of analysis is to
- The relation of this Laboratory Exerccise and the lecture discussed regarding Input/Process/Output is that the first order of business when approaching Spaatial Analysis is to know how to start. Understanding the format helps in selecting the best tool for our spatial analysis
- Selecting the correct format ensures smooth integration, data exchange, and optimal analysis.
- These formats, discussed last lecture, are crucial for storing, sharing, and processing geospatial data in GIS.
