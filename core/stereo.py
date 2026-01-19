def estimate_distance(bbox, metadata):
    if bbox is None:
        return None

    focal = metadata.get("focal_length_px")
    baseline = metadata.get("baseline_m")

    if not focal or not baseline:
        return None

    x1, y1, x2, y2 = bbox
    pixel_width = abs(x2 - x1)

    if pixel_width == 0:
        return None

    # Fake depth model (placeholder)
    return round((focal * baseline) / pixel_width, 2)
