"""
YOLO object detection module.
"""

from ultralytics import YOLO

# Load model once
_model = YOLO("yolov8n.pt")

def detect_objects(image):
    """
    image: numpy array (RGB or BGR)
    returns: list of detections
    """
    results = _model(image, verbose=False)

    detections = []

    for r in results:
        for box in r.boxes:
            detections.append({
                "class_id": int(box.cls[0]),
                "class_name": _model.names[int(box.cls[0])],
                "confidence": float(box.conf[0]),
                "bbox_xyxy": box.xyxy[0].tolist()
            })

    return detections
