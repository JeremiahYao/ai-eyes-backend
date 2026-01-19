from core.stereo import estimate_distance
from core.risk import assess_risk
from core.motion import analyze_motion
from core.detector import detect_objects

def run_navigation_pipeline(
    left_image,
    right_image,
    metadata,
    prev_results=None
):
    detections = detect_objects(left_image)
    results = []

    for det in detections:
        # Accept both formats just in case
        label = det.get("object") or det.get("label")
        confidence = det.get("confidence", 0.0)
        bbox = det.get("bbox")

        if label is None:
            continue

        distance = estimate_distance(bbox, metadata)
        risk = assess_risk(label, distance)
        motion = analyze_motion(label, bbox, prev_results)

        results.append({
            "object": label,
            "confidence": confidence,
            "distance_m": distance,
            "risk": risk,
            "motion": motion
        })

    return results
