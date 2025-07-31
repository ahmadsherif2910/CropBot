import cv2
import numpy as np


def remove_background(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)
    return mask


def extract_largest_region(image, mask):
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None

    largest = max(contours, key=cv2.contourArea)
    rect = cv2.minAreaRect(largest)
    box = cv2.boxPoints(rect).astype(int)

    width = int(rect[1][0])
    height = int(rect[1][1])
    if width == 0 or height == 0:
        return None

    src_pts = box.astype("float32")
    dst_pts = np.array([
        [0, height-1],
        [0, 0],
        [width-1, 0],
        [width-1, height-1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    cropped = cv2.warpPerspective(image, M, (width, height))
    return cropped
