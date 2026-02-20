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
- The difference between storing geometry in PostGIS is that this open source stores the data while GeoPandas represents the data.
- This is considered as input because no analysis has been done. The idea of analysis is to
- The relation of this Laboratory Exerccise and the lecture discussed regarding Input/Process/Output is that the first order of business when approaching Spaatial Analysis is to know how to start. Understanding the format helps in selecting the best tool for our spatial analysis
- Selecting the correct format ensures smooth integration, data exchange, and optimal analysis.
- These formats, discussed last lecture, are crucial for storing, sharing, and processing geospatial data in GIS.


## Reflection -- Process Reflection Milestone
- CRS transformation is necessary before area computation to make sure that the unit used is correct and to avoid distortion and inaccurate representation of data that may result to 
- Classification is part of the analysis process because it converts continuous values, such as percentage cover or density, into clear categories that are easier to interpret. It is more than just a visualization stage because classifying numerical findings helps in decision-making and helps uncover spatial patterns. 
- However, classification can be affected by sliver polygons and topology errors. Very small polygons created during overlay operations may distort area calculations and influence which class a feature is assigned to, while gaps or overlaps between polygons can lead to error in which class a feature is assigned to.
- Also, changing the dominance threshold can significantly modify spatial patterns. If the percentage required to define dominance is adjusted, different areas may fall into different categories, which can alter the overall interpretation and conclusions of the analysis.

## Reflection - Challenge Task
- The spatial question I choose is the identification of parcels where Non-Residential landuse occupies ≥ 50% of the parcel area, which is the Option 1 - Dominant Non-Residential Parcels
- Following the lab manual and understanding the content help me come up with my algorithm steps which is to edit the given script from the lab manual.
- h difference between my script is the parameter needed for the challenge. The design and implementation for the spatial analysis used is to identify parcels where Non-Residential landuse occupies ≥ 50% of the parcel area and the way I come up woth my script is to edit the given script from the manual based on the parameter needed.
