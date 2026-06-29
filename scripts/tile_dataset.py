import os
import rasterio
from rasterio.windows import Window
from PIL import Image
import numpy as np

TIF_PATH = r"C:\Users\anushi.aggarwal\Desktop\tif_pred_orig\2.tif"
MASK_PATH = r"road_mask.tif"

TILE_SIZE = 512

os.makedirs("dataset/images", exist_ok=True)
os.makedirs("dataset/masks", exist_ok=True)

tile_count = 0

with rasterio.open(TIF_PATH) as img_src, rasterio.open(MASK_PATH) as mask_src:

    width = img_src.width
    height = img_src.height

    for y in range(0, height, TILE_SIZE):
        for x in range(0, width, TILE_SIZE):

            if x + TILE_SIZE > width or y + TILE_SIZE > height:
                continue

            window = Window(x, y, TILE_SIZE, TILE_SIZE)

            image_tile = img_src.read(
                [1, 2, 3],
                window=window
            )

            mask_tile = mask_src.read(
                1,
                window=window
            )

            image_tile = image_tile.transpose((1, 2, 0))

            image_tile = image_tile.astype(np.uint8)
            mask_tile = (mask_tile * 255).astype(np.uint8)

            Image.fromarray(image_tile).save(
                f"dataset/images/tile_{tile_count:05d}.png"
            )

            Image.fromarray(mask_tile).save(
                f"dataset/masks/tile_{tile_count:05d}.png"
            )

            tile_count += 1

print(f"Created {tile_count} tiles")