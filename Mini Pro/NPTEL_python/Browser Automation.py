import cv2
import numpy as np
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from skimage import measure

def analyze_leaf_image(image_path):
    # --- Load image ---
    image = Image.open(image_path).convert("RGB")
    img_cv = cv2.imread(image_path)

    # --- Load BLIP model for image captioning ---
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # --- Step 1: AI Caption (scene description) ---
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=80)
    caption = processor.decode(output[0], skip_special_tokens=True)

    # --- Step 2: Color Analysis ---
    img_hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
    avg_color = cv2.mean(img_cv)[:3]
    avg_color_hex = "#{:02x}{:02x}{:02x}".format(int(avg_color[2]), int(avg_color[1]), int(avg_color[0]))

    # --- Step 3: Texture Analysis ---
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    texture = cv2.Laplacian(gray, cv2.CV_64F).var()
    texture_desc = "smooth" if texture < 100 else "slightly rough" if texture < 300 else "rough"

    # --- Step 4: Shape / Contour Analysis ---
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    circularity = (4 * np.pi * area) / (perimeter ** 2)
    shape_desc = (
        "round" if circularity > 0.8 else
        "oval" if circularity > 0.5 else
        "irregular"
    )

    # --- Step 5: Compile Description ---
    description = f"""
🔍 **Leaf Image Analysis**
AI Caption: {caption}

**Visual Attributes:**
- Dominant Color: {avg_color_hex}
- Texture: {texture_desc}
- Shape: {shape_desc}
- Circularity Index: {circularity:.2f}

**Interpretation:**
This appears to be a {shape_desc} leaf with a {texture_desc} surface and an average color tone near {avg_color_hex}.
AI vision describes it as: "{caption}".
If discolorations or holes are visible, they might indicate stress or disease.
"""

    return description.strip()


# --- Example Usage ---
if __name__ == "__main__":
    path = "D:\Studies\Projects\Python\Mini Pro\Images\kt-201904153.jpeg"   # put your leaf image here
    result = analyze_leaf_image(path)
    print(result)
