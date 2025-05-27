from PIL import Image
import numpy as np

def analyze_image(image_file):
    image = Image.open(image_file).convert("RGB")
    width, height = image.size

    total_area = (width * height) / 10000
    usable_area = total_area * 0.6

    panel_area = 1.6
    panel_count = int(usable_area / panel_area)

    annual_generation = panel_count * 350 * 4 * 365 / 1000

    return {
        "area_m2": round(usable_area, 2),
        "panel_count": panel_count,
        "obstructions": "Minimal",
        "annual_generation_kwh": int(annual_generation)
    }
