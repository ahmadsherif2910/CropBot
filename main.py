import os
import cv2
from config import *
from yolo import detect_objects
from removeBG import remove_background, extract_largest_region
from orientation import correct_orientation

# Toggles to control optional saves
SAVE_CROPPED = False
SAVE_ALIGNED = False

# Main processing loop
for filename in os.listdir(photos_folder):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    full_path = os.path.join(photos_folder, filename)
    print(f"\n📷 Processing {filename}...")

    boxes = detect_objects(full_path)
    image = cv2.imread(full_path)

    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = map(int, box)
        crop = image[y1:y2, x1:x2]
        crop_name = f"{os.path.splitext(filename)[0]}_crop{i}.jpg"

        if SAVE_CROPPED:
            cv2.imwrite(os.path.join(cropped_folder, crop_name), crop)

        mask = remove_background(crop)
        aligned = extract_largest_region(crop, mask)
        if aligned is None:
            print(f"⚠️ Skipped {crop_name}: no valid region found.")
            continue

        if SAVE_ALIGNED:
            cv2.imwrite(os.path.join(aligned_folder, crop_name), aligned)

        fixed = correct_orientation(aligned)
        cv2.imwrite(os.path.join(final_folder, crop_name), fixed)

        print(f"✅ Saved: {os.path.join(final_folder, crop_name)}")
