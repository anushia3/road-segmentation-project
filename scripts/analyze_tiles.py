import os
from PIL import Image
import numpy as np

mask_dir = "dataset/masks"

empty_tiles = 0
road_tiles = 0

for file in os.listdir(mask_dir):

    mask = np.array(
        Image.open(
            os.path.join(mask_dir, file)
        )
    )

    if mask.sum() == 0:
        empty_tiles += 1
    else:
        road_tiles += 1

print("Road tiles:", road_tiles)
print("Empty tiles:", empty_tiles)

print(
    "Road tile percentage:",
    100 * road_tiles / (road_tiles + empty_tiles)
)