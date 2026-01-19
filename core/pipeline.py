"""
Main processing pipeline for AI Eyes backend.

This file connects:
- Object detection (YOLO)
- Stereo distance estimation (parallax / trigonometry)
- Navigation-level output (objects + distances)

No API, no hosting logic here.
"""

from core.detector import detect_objects
from core.stereo import estimate_distance


def process_frame(image, camera_id, metadata=None):
    """
    Basic single-frame processor (used for testing / extension).

    image: numpy image
    camera_id: 'left', 'right', or 'rear'
    metadata: dictionary (focal length, baseline, etc.)
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
    Full navigation pipeline using stereo vision.

    Steps:
    1. Detect objects in left & right images
    2. Match detections (simple version)
    3. Estimate distance using disparity
    4. Return navigation-ready results
    """

    # Run object detection
    detections_left = detect_objects(left_image)
    detections_right = detect_objects(right_image)

    results = []

    # ⚠️ Temporary simple matching using zip
    # (Will be improved later with proper object matching)
    for dl, dr in zip(detections_left, detections_right):

        # Bounding box center x-coordinates
        x_left = (dl["bbox_xyxy"][0] + dl["bbox_xyxy"][2]) / 2
        x_right = (dr["bbox_xyxy"][0] + dr["bbox_xyxy"][2]) / 2

        distance = estimate_distance(
            x_left=x_left,
            x_right=x_right,
            focal_length_px=metadata["focal_length_px"],
            baseline_m=metadata["baseline_m"]
        )

        results.append({
            "object": dl["class_name"],
            "confidence": dl["confidence"],
            "distance_m": distance
        })

    return results
