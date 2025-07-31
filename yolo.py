from ultralytics import YOLO

# Load the trained YOLO model once
model = YOLO("notebook/runs/detect/train5/weights/best.pt")


def detect_objects(image_path):
    results = model.predict(source=image_path, conf=0.02)[0]
    return results.boxes.xyxy.cpu().numpy()
