from datetime import datetime
from pathlib import Path

INPUT_FILE = ""
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILEPATH = ""
ISO_DATE_FORMAT = "%y%m%dT%H:%M"
current_date = datetime.now().strftime(ISO_DATE_FORMAT)
