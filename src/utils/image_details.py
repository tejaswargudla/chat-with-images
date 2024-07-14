import exif
from datetime import datetime

def get_metadata(filepath):
    try:
        image = exif.Image(filepath)
        image_created_dt = datetime.strptime(image.datetime, "%Y:%m:%d %H:%H:%S")
        description = f"This image got created or shot on this year {image_created_dt.year}."
        return description
    except FileNotFoundError as exce:
        return False
    except Exception as exce:
        return False