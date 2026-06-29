import rasterio

TIF_PATH = r"C:\Users\anushi.aggarwal\Desktop\tif_pred_orig\2.tif"

with rasterio.open(TIF_PATH) as src:
    image = src.read([1, 2, 3])

print("Shape:", image.shape)
print("Min:", image.min())
print("Max:", image.max())
print("Datatype:", image.dtype)