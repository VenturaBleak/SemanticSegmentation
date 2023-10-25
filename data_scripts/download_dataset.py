import requests
import tarfile
import os
from tqdm import tqdm

from data_config import DATA_DIRECTORY, TAR_FILE, EXTRACTED_FOLDER

# Driectories
data_directory = DATA_DIRECTORY
tar_file = TAR_FILE
extracted_folder = EXTRACTED_FOLDER

# Create data_directory if it doesn't exist
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

# Download the dataset only if it hasn't been extracted
if not os.path.exists(extracted_folder):
    url = "http://dags.stanford.edu/data/iccv09Data.tar.gz"

    print(f"Downloading {url} to {tar_file}")

    response = requests.get(url, stream=True)

    # Save the downloaded content to tar_file
    with open(tar_file, 'wb') as f:
        for chunk in tqdm(response.iter_content(chunk_size=8192)):
            f.write(chunk)

    # Ensure we got a good response before extracting
    if response.status_code == 200:
        print(f"Download complete. Extracting {tar_file} to {data_directory}")

        with tarfile.open(tar_file, 'r:gz') as tar:
            tar.extractall(path=data_directory)
    else:
        print(f"Failed to download the dataset. HTTP Response Code: {response.status_code}")

else:
    print(f"Dataset already exists in {extracted_folder}")


# Preview the dataset
# randomly select an image from the dataset
import mmcv
import matplotlib.pyplot as plt
import random

# randomly select an image from the dataset
sample_img = random.choice(os.listdir(os.path.join(extracted_folder, "images")))
img = mmcv.imread(os.path.join(extracted_folder, "images", sample_img))

# show the image
plt.figure(figsize=(8, 6))
plt.imshow(mmcv.bgr2rgb(img))
plt.show()