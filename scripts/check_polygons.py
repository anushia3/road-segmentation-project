import geopandas as gpd
import matplotlib.pyplot as plt

SHP_PATH = r"C:\Users\anushi.aggarwal\Desktop\road_training_data\road_td.shp"

roads = gpd.read_file(SHP_PATH)

print(roads.head())

roads.plot(figsize=(8,8))
plt.show()