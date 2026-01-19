"""
Main processing pipeline for AI Eyes backend.

This file CONNECTS:
- Object detection (YOLO)
- Stereo distance estimation (parallax / trigonometry)
- Risk assessment
- Navigation-level output

NO API
NO hosting
NO UI
"""

from .detector import detect_objects
from .stereo import estimate_distance
from .risk import assess_risk


def process_frame(image, camera_id, metadata=None):
    """
    Single-frame processor.
    Used for testing or single-camera (e.g. rear camera).

    image: numpy array
    camera_id: 'left', 'right', or 'rear'
    metadata: optional dictionary
    """
    if metadata is None:
        metadata = {}

    detections = detect_objects(image)

    return {
        "camera_id": camera_id,
        "detections": detections
    }


def run_navigation_pipeline(left_image, right_image, metadata):
    """
    Full stereo navigation pipeline.

    Steps:
    1. Detect objects in left image
    2. Detect objects in right image
    3. Estimate distance using parallax
    4. Assess risk
    5. Return navigation-ready output
    """

    # 1️⃣ Object detection
    detections_left = detect_objects(left_image)
    detections_right = detect_objects(right_image)

    results = []

    # 2️⃣ TEMPORARY simple matching (by index)
    # Later this will be replaced with proper matching logic
    num_pairs = min(len(detections_left), len(detections_right))

    for i in range(num_pairs):
        dl = detections_left[i]
        dr = detections_right[i]

        # 3️⃣ Compute x-center of bounding boxes
        x_left = (dl["bbox_xyxy"][0] + dl["bbox_xyxy"][2]) / 2
        x_right = (dr["bbox_xyxy"][0] + dr["bbox_xyxy"][2]) / 2

        # 4️⃣ Distance estimation (TRIGONOMETRY happens here)
        distance = estimate_distance(
            x_left=x_left,
            x_right=x_right,
            focal_length_px=metadata["focal_length_px"],
            baseline_m=metadata["baseline_m"]
        )

        # 5️⃣ Risk assessment
        risk = assess_risk(dl["class_name"], distance)

        # 6️⃣ Navigation-level output
        results.append({
            "object": dl["class_name"],
            "confidence": dl["confidence"],
            "distance_m": distance,
            "risk": risk
        })

    return results
