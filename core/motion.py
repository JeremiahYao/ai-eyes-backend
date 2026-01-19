def analyze_motion(label, bbox, prev_results):
    # No previous frame → stationary
    if not prev_results:
        return "stationary"

    for prev in prev_results:
        if prev.get("object") == label:
            return "moving"

    return "stationary"
