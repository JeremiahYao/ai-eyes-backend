"""
Main processing pipeline for AI Eyes backend.

This pipeline connects:
- Object detection (YOLO)
- Stereo distance estimation (placeholder for now)
- Risk assessment
- Temporal motion estimation (approaching / receding / stationary)

No API, no hosting logic here.
"""

from .detector import detect_objects
from .stereo import estimate_distance
from .risk import assess_risk
from .motion import estimate_motion

# ------------------------------------------------------------------
# Simple global memory for previous frame (Step 11)
# ------------------------------------------------------------------
_previous_bboxes = {}


def process_frame(image, camera_id, metadata=None):
    """
    Basic single-frame processor (used for testing / extension).

    image: numpy image
    camera_id: 'left', 'right', or 'rear'
    metadata: dictionary (optional)
    """
    detections = detect_objects(image)

    return {
        "camera_id": camera_id,
        "detections": detections
    }


def run_navigation_pipeline(left_image, right_image, metadata):
    """
    Full navigation pipeline.

    Steps:
    1. Detect objects
    2. (Optional) Stereo distance estimation
    3. Risk assessment
    4. Temporal motion estimation (Step 11)
    """

    global _previous_bboxes

    detections_left = detect_objects(left_image)

    results = []

    for idx, det in enumerate(detections_left):
        class_name = det["class_name"]
        confidence = det["confidence"]
        bbox = det["bbox_xyxy"]

        # ----------------------------------------------------------
        # Distance estimation (disabled for now)
        # ----------------------------------------------------------
        distance_m = None  # expected to be None at this stage

        # ----------------------------------------------------------
        # Risk assessment
        # ----------------------------------------------------------
        risk = assess_risk(class_name, distance_m)

        # ----------------------------------------------------------
        # Motion estimation (Step 11)
        # ----------------------------------------------------------
        prev_bbox = _previous_bboxes.get(idx)
        motion = estimate_motion(prev_bbox, bbox)

        # Save bbox for next frame
        _previous_bboxes[idx] = bbox

        results.append({
            "object": class_name,
            "confidence": confidence,
            "distance_m": distance_m,
            "risk": risk,
            "motion": motion
        })

    return results
