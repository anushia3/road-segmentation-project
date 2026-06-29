import rasterio
import geopandas as gpd

TIF_PATH = r"C:\Users\anushi.aggarwal\Desktop\tif_pred_orig\2.tif"
SHP_PATH = r"C:\Users\anushi.aggarwal\Desktop\road_training_data\road_td.shp"

print("=== TIFF INFO ===")

with rasterio.open(TIF_PATH) as src:
    print("Width:", src.width)
    print("Height:", src.height)
    print("Bands:", src.count)
    print("CRS:", src.crs)
    print("Bounds:", src.bounds)

print("\n=== SHAPEFILE INFO ===")

roads = gpd.read_file(SHP_PATH)

print("CRS:", roads.crs)
print("Number of features:", len(roads))
print("Geometry types:")
print(roads.geometry.geom_type.value_counts())
print("\nColumns:")
print(roads.columns.tolist())