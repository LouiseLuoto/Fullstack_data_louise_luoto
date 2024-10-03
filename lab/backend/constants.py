from pathlib import Path


DATABASE_PATH = Path(__file__).parents[2] / "lab" / "backend" / "youtube_data.db"
CLEANED_DATA_PATH = Path(__file__).parent / "cleaned_data"
RAW_DATA_PATH = Path(__file__).parents[2] / "lab_overview" / "backend" / "raw_data"