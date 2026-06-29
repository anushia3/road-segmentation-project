import os
import random
import shutil

random.seed(42)

IMAGE_DIR = "dataset/images"
MASK_DIR = "dataset/masks"

TRAIN_IMAGE_DIR = "dataset/train/images"
TRAIN_MASK_DIR = "dataset/train/masks"

VAL_IMAGE_DIR = "dataset/val/images"
VAL_MASK_DIR = "dataset/val/masks"

os.makedirs(TRAIN_IMAGE_DIR, exist_ok=True)
os.makedirs(TRAIN_MASK_DIR, exist_ok=True)
os.makedirs(VAL_IMAGE_DIR, exist_ok=True)
os.makedirs(VAL_MASK_DIR, exist_ok=True)

files = sorted(os.listdir(IMAGE_DIR))

random.shuffle(files)

split_idx = int(0.8 * len(files))

train_files = files[:split_idx]
val_files = files[split_idx:]

for file in train_files:

    shutil.copy(
        os.path.join(IMAGE_DIR, file),
        os.path.join(TRAIN_IMAGE_DIR, file)
    )

    shutil.copy(
        os.path.join(MASK_DIR, file),
        os.path.join(TRAIN_MASK_DIR, file)
    )

for file in val_files:

    shutil.copy(
        os.path.join(IMAGE_DIR, file),
        os.path.join(VAL_IMAGE_DIR, file)
    )

    shutil.copy(
        os.path.join(MASK_DIR, file),
        os.path.join(VAL_MASK_DIR, file)
    )

print("Train:", len(train_files))
print("Validation:", len(val_files))