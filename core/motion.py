# core/motion.py

def analyze_motion(label, bbox, prev_results=None):
    """
    Very simple motion analysis.
    If no previous frame data exists, return 'stationary'.
    """

    if prev_results is None:
        return "stationary"

    # Try to find the same object in previous frame
    for prev in prev_results:
        if prev.get("object") == label:
            prev_bbox = prev.get("bbox")
            if prev_bbox and bbox:
                # Simple area comparison
                prev_area = (prev_bbox[2] - prev_bbox[0]) * (prev_bbox[3] - prev_bbox[1])
                curr_area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])

                if curr_area > prev_area * 1.1:
                    return "approaching"
                elif curr_area < prev_area * 0.9:
                    return "moving away"

    return "stationary"
