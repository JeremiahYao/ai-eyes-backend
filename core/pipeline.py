from core.detector import detect_objects
from core.stereo import estimate_distance
from core.risk import compute_risk

def run_navigation_pipeline(left_image, right_image, metadata):
    detections_left = detect_objects(left_image)
    detections_right = detect_objects(right_image)

    results = []
    min_len = min(len(detections_left), len(detections_right))

    for i in range(min_len):
        dl = detections_left[i]
        dr = detections_right[i]

        x_left = (dl["bbox_xyxy"][0] + dl["bbox_xyxy"][2]) / 2
        x_right = (dr["bbox_xyxy"][0] + dr["bbox_xyxy"][2]) / 2

        distance = estimate_distance(
            x_left,
            x_right,
            metadata["focal_length_px"],
            metadata["baseline_m"]
        )

        risk = compute_risk(
            distance,
            dl["confidence"],
            dl["class_name"]
        )

        results.append({
            "object": dl["class_name"],
            "distance_m": distance,
            "risk_score": risk
        })

    # sort by danger
    results.sort(key=lambda x: x["risk_score"], reverse=True)
    return results
