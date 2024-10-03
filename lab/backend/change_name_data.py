from shutil import copytree, rmtree
from constants import CLEANED_DATA_PATH, RAW_DATA_PATH


if CLEANED_DATA_PATH.is_dir():
    rmtree(CLEANED_DATA_PATH)

CLEANED_DATA_PATH.mkdir(parents=True, exist_ok=True)

for folder in RAW_DATA_PATH.iterdir():
    new_name = folder.name.split()[0]
    copytree(folder, CLEANED_DATA_PATH / new_name)