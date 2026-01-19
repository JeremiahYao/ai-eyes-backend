# core/pipeline.py

from core.detector import detect_objects
from core.stereo import estimate_distance
from core.risk import assess_risk
from core.motion import analyze_motion


def run_navigation_pipeline(left_image, right_image, metadata, prev_results=None):
    """
    Main perception pipeline.
    """

    detections = detect_objects(left_image)
    results = []

    for det in detections:
        label = det["label"]
        confidence = det["confidence"]
        bbox = det.get("bbox")

        # Distance estimation (may return None)
        distance = estimate_distance(
            bbox=bbox,
            left_image=left_image,
            right_image=right_image,
            metadata=metadata
        )

        # Risk assessment MUST allow None
        risk = assess_risk(label, distance)

        # Motion (safe even if bbox is None)
        motion = analyze_motion(
            label=label,
            bbox=bbox,
            prev_results=prev_results
        )

        results.append({
            "object": label,
            "confidence": confidence,
            "distance_m": distance,
            "risk": risk,
            "motion": motion
        })

    return results
