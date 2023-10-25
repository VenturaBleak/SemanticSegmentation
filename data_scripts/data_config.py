import os

# Directories and files
DATA_DIRECTORY = os.path.join("..","data", "stanford_background")
TAR_FILE = os.path.join(DATA_DIRECTORY, "stanford_background.tar.gz")
EXTRACTED_FOLDER = os.path.join(DATA_DIRECTORY, "iccv09Data")

# Define classes using nested dictionaries
CLASSES_DICT = {
    0: {'name': 'sky', 'rgb': [128, 128, 128]},
    1: {'name': 'tree', 'rgb': [129, 127, 38]},
    2: {'name': 'road', 'rgb': [120, 69, 125]},
    3: {'name': 'grass', 'rgb': [53, 125, 34]},
    4: {'name': 'water', 'rgb': [0, 11, 123]},
    5: {'name': 'bldg', 'rgb': [118, 20, 12]},
    6: {'name': 'mntn', 'rgb': [122, 81, 25]},
    7: {'name': 'fg_obj', 'rgb': [241, 134, 51]},
    255: {'name': 'unk', 'rgb': [0, 0, 0]}
}