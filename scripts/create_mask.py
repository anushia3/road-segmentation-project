import rasterio
import geopandas as gpd
from rasterio.features import rasterize
import numpy as np

TIF_PATH = r"C:\Users\anushi.aggarwal\Desktop\tif_pred_orig\2.tif"
SHP_PATH = r"C:\Users\anushi.aggarwal\Desktop\road_training_data\road_td.shp"

roads = gpd.read_file(SHP_PATH)

with rasterio.open(TIF_PATH) as src:
    transform = src.transform
    height = src.height
    width = src.width
    profile = src.profile

mask = rasterize(
    [(geom, 1) for geom in roads.geometry],
    out_shape=(height, width),
    transform=transform,
    fill=0,
    dtype=np.uint8
)

profile.update(
    count=1,
    dtype=rasterio.uint8
)

with rasterio.open("road_mask.tif", "w", **profile) as dst:
    dst.write(mask, 1)

print("Mask saved as road_mask.tif")
print("Mask shape:", mask.shape)
print("Road pixels:", mask.sum())