import rasterio
import matplotlib.pyplot as plt

MASK_PATH = r"road_mask.tif"

with rasterio.open(MASK_PATH) as src:
    mask = src.read(1)

crop = mask[0:2000, 0:2000]

plt.imshow(crop, cmap="gray")
plt.title("Mask Crop")
plt.show()