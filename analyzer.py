from PIL import Image
import numpy as np

def analyze_image(image_file):
    image = Image.open(image_file).convert("L")  # Convert to grayscale
    image = image.resize((300, 300))  # Normalize size
    np_img = np.array(image)

    brightness = np.mean(np_img)
    obstruction_level = "High" if brightness < 80 else "Moderate" if brightness < 140 else "Low"

    # Assume total rooftop area per image (scaled): 100 m²
    base_area = 100
    usable_ratio = 0.5 if obstruction_level == "High" else 0.6 if obstruction_level == "Moderate" else 0.75
    usable_area = base_area * usable_ratio

    panel_area = 1.6  # in m²
    panel_count = int(usable_area / panel_area)

    annual_generation = panel_count * 350 * 4 * 365 / 1000  # realistic estimate

    return {
        "usable_area_m2": round(usable_area, 2),
        "panel_count": panel_count,
        "obstructions": obstruction_level,
        "annual_generation_kwh": int(annual_generation)
    }
