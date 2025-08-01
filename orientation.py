# import cv2
# from utils import rotate_image

# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# def detect_faces(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(
#         gray, scaleFactor=1.1, minNeighbors=5)
#     return len(faces)


# def correct_orientation(image):
#     max_faces = -1
#     best_image = image

#     for angle in [0, 90, 180, 270]:
#         rotated = rotate_image(image, angle)
#         face_count = detect_faces(rotated)

#         if face_count > max_faces:
#             max_faces = face_count
#             best_image = rotated

#     return best_image

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Define your rotation helper


def rotate_image(img, angle):
    if angle == 90:
        return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    elif angle == 180:
        return cv2.rotate(img, cv2.ROTATE_180)
    elif angle == 270:
        return cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return img

# Orientation correction function


def correct_orientation(img, model):
    angle_map = {0: 0, 1: 90, 2: 180, 3: 270}

    # Resize and normalize the image
    img_resized = tf.image.resize(img, (256, 256))
    img_normalized = img_resized / 255.0
    input_image = np.expand_dims(img_resized, 0)
    # np.expand_dims(img_normalized, axis=0)
# resize = tf.image.resize(img,(256,256))
# plt.imshow(resize.numpy().astype(int))
# plt.show()
    # Predict orientation
    predictions = model.predict(np.expand_dims(img_resized/255, 0))
    predicted_class = np.argmax(predictions)
    predicted_angle = angle_map[predicted_class]

    # Rotate the image accordingly
    corrected_img = rotate_image(img, predicted_angle)
    return corrected_img
