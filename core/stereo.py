# core/stereo.py

"""
Distance estimation (monocular fallback).
"""

# Average real-world object heights (meters)
KNOWN_HEIGHTS_M = {
    "person": 1.7,
    "car": 1.5,
    "bus": 3.2,
    "truck": 3.0,
    "bicycle": 1.5,
    "motorcycle": 1.4,
    "traffic light": 3.0
}

def estimate_distance(bbox, object_name, metadata):
    """
    Estimate distance using bounding box height.

    bbox: [x1, y1, x2, y2]
    metadata: {
        "focal_length_px": int,
        "baseline_m": float (unused for now)
    }
    """
    if bbox is None:
        return None

    real_height = KNOWN_HEIGHTS_M.get(object_name)
    if real_height is None:
        return None

    focal_length = metadata.get("focal_length_px")
    if focal_length is None:
        return None

    pixel_height = bbox[3] - bbox[1]
    if pixel_height <= 0:
        return None

    distance_m = (real_height * focal_length) / pixel_height
    return round(distance_m, 2)
