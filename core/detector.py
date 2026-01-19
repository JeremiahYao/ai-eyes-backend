from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(image):
    results = model(image)[0]
    detections = []

    for box in results.boxes:
        detections.append({
            "object": model.names[int(box.cls)],
            "confidence": float(box.conf),
            "bbox": box.xyxy[0].tolist()
        })

    return detections
