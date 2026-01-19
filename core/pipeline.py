# core/pipeline.py

"""
Main navigation perception pipeline.
"""

from core.detector import detect_objects
from core.stereo import estimate_distance
from core.risk import assess_risk
from core.motion import analyze_motion


def run_navigation_pipeline(left_image, right_image, metadata):
    """
    Runs the full perception pipeline on one frame.
    """

    detections = detect_objects(left_image)

    results = []

    for det in detections:
        obj_name = det.get("object")
        confidence = det.get("confidence")
        bbox = det.get("bbox")

        # --- Distance estimation ---
        distance_m = estimate_distance(
            bbox=bbox,
            object_name=obj_name,
            metadata=metadata
        )

        # --- Risk assessment ---
        risk = assess_risk(obj_name, distance_m)

        result = {
            "object": obj_name,
            "confidence": confidence,
            "distance_m": distance_m,
            "risk": risk,
            "bbox": bbox
        }

        results.append(result)

    # --- Motion analysis (optional, safe) ---
    try:
        results = analyze_motion(results)
    except Exception:
        for r in results:
            r["motion"] = "unknown"

    return results
