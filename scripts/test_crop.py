import rasterio
import matplotlib.pyplot as plt

TIF_PATH = r"C:\Users\anushi.aggarwal\Desktop\tif_pred_orig\2.tif"

with rasterio.open(TIF_PATH) as src:
    image = src.read([1, 2, 3])

image = image.transpose((1, 2, 0))

# Take a small crop
crop = image[0:2000, 0:2000]

plt.imshow(crop)
plt.title("Image Crop")
plt.show()