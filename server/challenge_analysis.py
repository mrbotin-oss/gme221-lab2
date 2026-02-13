import geopandas as gpd
from sqlalchemy import create_engine

# Database connection parameters
host = "localhost"
port = "5432"
dbname = "gme221"
user = "postgres"
password = "#Akonaito1234"

# Create connection string
conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

#Create SQLAlchemy engine
engine = create_engine(conn_str)

# Minimal SQL queries (no spatial operations)
sql_parcel = "SELECT parcel_pin, geom FROM public.parcel"
sql_landuse = "SELECT name, geom FROM public.landuse"

# Load data into GeoDataFrames
parcel = gpd.read_postgis(sql_parcel, engine, geom_col="geom")
landuse = gpd.read_postgis(sql_landuse, engine, geom_col="geom")

parcel = parcel.to_crs(epsg=3395)
landuse = landuse.to_crs(epsg=3395)

parcel["total_area"] = parcel.geometry.area

overlay = gpd.overlay(parcel, landuse, how="intersection")
overlay["landuse_area"] = overlay.geometry.area

overlay["percentage"] = (
    overlay["landuse_area"] / overlay["total_area"]
) * 100

overlay["percentage"] = overlay["percentage"].round(2)

dominant_nonres = overlay[
    (~(overlay["name"] == "Residential Zone - Low Density") |
    (overlay["name"] == "Residential Zone - Medium Density")) &
    (overlay["percentage"] >= 50)
].copy()

print (dominant_nonres.head())

dominant_nonres = dominant_nonres.to_crs(epsg=4326)

dominant_nonres.to_file(
    "output/challenge_result.geojson",
    driver="GeoJSON"
)

print("GeoJSON saved successfully")
