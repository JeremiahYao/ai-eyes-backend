# core/stereo.py

def estimate_distance(bbox, metadata):
    """
    Simple monocular approximation.
    """
    if bbox is None:
        return None

    focal = metadata.get("focal_length_px")
    baseline = metadata.get("baseline_m")

    if focal is None or baseline is None:
        return None

    x1, y1, x2, y2 = bbox
    width = max(1, x2 - x1)

    distance = (focal * baseline) / width

    # 🔒 Sanity clamp
    distance = max(0.5, min(distance, 50.0))

    return round(distance, 2)
