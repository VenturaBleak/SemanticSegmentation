import numpy as np
from PIL import Image
import os
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from data_config import EXTRACTED_FOLDER, CLASSES_DICT

# Define directory paths
data_directory = EXTRACTED_FOLDER
ann_dir = os.path.join(data_directory, "labels")
img_dir = os.path.join(data_directory, "images")

# Instead of mmcv.scandir, we'll use os.listdir and filter by suffix
for filename in os.listdir(ann_dir):
    if filename.endswith('.regions.txt'):
        seg_map = np.loadtxt(os.path.join(ann_dir, filename)).astype(np.uint8)

        # Check for unexpected class values
        unexpected_values = set(np.unique(seg_map)) - set(CLASSES_DICT.keys())
        assert set(np.unique(seg_map)) <= set(CLASSES_DICT.keys()), f"Unexpected class values in {filename}: {unexpected_values}."

        # Convert segmentation map to RGB using the color map
        h, w = seg_map.shape
        rgb_image = np.zeros((h, w, 3), dtype=np.uint8)
        for i in range(h):
            for j in range(w):
                rgb_image[i, j] = CLASSES_DICT[seg_map[i, j]]['rgb']

        # Convert RGB numpy array to PIL Image and save
        seg_img = Image.fromarray(rgb_image)
        seg_img.save(os.path.join(ann_dir, filename.replace('.regions.txt', '.png')))

        print(f"Converted {filename} to {filename.replace('.regions.txt', '.png')}")

# randomly sample from the png files in the annotation directory
sample_img_name = random.choice([f for f in os.listdir(ann_dir) if f.endswith('.png')])
label_img = Image.open(os.path.join(ann_dir, sample_img_name))
original_img = Image.open(os.path.join(img_dir, sample_img_name.replace('.png', '.jpg')))

# Create a figure and a 1x2 subplot (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Display original image in the first subplot
axes[0].imshow(original_img)
axes[0].axis('off')
axes[0].set_title('Original Image')

# Display label in the second subplot
axes[1].imshow(np.array(label_img.convert('RGB')))
axes[1].axis('off')
axes[1].set_title('Segmentation Label')

# Create a patch (proxy artist) for every color
patches = [mpatches.Patch(color=np.array(CLASSES_DICT[i]['rgb']) / 255.,
                            label=CLASSES_DICT[i]['name']) for i in CLASSES_DICT.keys()]

# Adjust legend placement
fig.legend(handles=patches, bbox_to_anchor=(0.5, 0.97), loc='upper center', borderaxespad=0., fontsize='large', ncol=len(CLASSES_DICT.keys()))

plt.tight_layout()
plt.show()