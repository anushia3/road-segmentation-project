import rasterio
import geopandas as gpd
import matplotlib.pyplot as plt

TIF_PATH = r"C:\Users\anushi.aggarwal\Desktop\tif_pred_orig\2.tif"
SHP_PATH = r"C:\Users\anushi.aggarwal\Desktop\road_training_data\road_td.shp"

roads = gpd.read_file(SHP_PATH)

with rasterio.open(TIF_PATH) as src:
    image = src.read([1, 2, 3])

image = image.transpose((1, 2, 0))

plt.figure(figsize=(12, 12))
plt.imshow(image)

roads.boundary.plot(
    ax=plt.gca(),
    color="red",
    linewidth=1
)

plt.title("Road Polygons Over Satellite Image")
plt.show()