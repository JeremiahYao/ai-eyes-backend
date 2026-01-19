"""
Main processing pipeline for AI Eyes backend.
Connects detection, stereo (optional), risk, motion, and semantics.
"""

from .detector import detect_objects
from .stereo import estimate_distance
from .risk import assess_risk


# ---------- Helpers ----------

def estimate_direction(bbox, image_width):
    if bbox is None:
        return "unknown"

    x1, _, x2, _ = bbox
    x_center = (x1 + x2) / 2
    ratio = x_center / image_width

    if ratio < 0.33:
        return "left"
    elif ratio < 0.66:
        return "center"
    else:
        return "right"


def estimate_distance_bucket(bbox):
    if bbox is None:
        return "unknown"

    x1, y1, x2, y2 = bbox
    area = (x2 - x1) * (y2 - y1)

    if area > 40000:
        return "near"
    elif area > 15000:
        return "medium"
    else:
        return "far"


# ---------- Pipeline ----------

def run_navigation_pipeline(left_image, right_image, metadata):
    """
    Full navigation pipeline.
    """

    detections_left = detect_objects(left_image)
    detections_right = detect_objects(right_image)

    results = []

    for dl, dr in zip(detections_left, detections_right):

        bbox_l = dl.get("bbox_xyxy")

        # Stereo distance (optional)
        distance = None
        if bbox_l is not None and "focal_length_px" in metadata:
            x_left = (bbox_l[0] + bbox_l[2]) / 2
            x_right = x_left  # temporary fallback
            distance = estimate_distance(
                x_left=x_left,
                x_right=x_right,
                focal_length_px=metadata["focal_length_px"],
                baseline_m=metadata["baseline_m"]
            )

        direction = estimate_direction(bbox_l, left_image.shape[1])
        distance_bucket = estimate_distance_bucket(bbox_l)
        risk = assess_risk(dl["class_name"], distance)

        results.append({
            "object": dl["class_name"],
            "confidence": dl["confidence"],
            "distance_m": distance,
            "distance_bucket": distance_bucket,
            "direction": direction,
            "risk": risk
        })

    return results
