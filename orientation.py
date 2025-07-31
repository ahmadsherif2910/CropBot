import cv2
from utils import rotate_image

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5)
    return len(faces)


def correct_orientation(image):
    best_angle = 0
    max_faces = -1
    best_image = image

    for angle in [0, 90, 180, 270]:
        rotated = rotate_image(image, angle)
        face_count = detect_faces(rotated)
        if face_count > max_faces:
            max_faces = face_count
            best_angle = angle
            best_image = rotated

    return best_image
