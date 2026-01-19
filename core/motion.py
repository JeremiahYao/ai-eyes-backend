"""
Motion estimation using bounding box size changes.
"""

def estimate_motion(prev_bbox, curr_bbox, threshold=0.05):
    """
    prev_bbox, curr_bbox: [x1, y1, x2, y2] or None
    """

    # ✅ First frame or missing data
    if prev_bbox is None or curr_bbox is None:
        return "unknown"

    def area(b):
        return (b[2] - b[0]) * (b[3] - b[1])

    prev_area = area(prev_bbox)
    curr_area = area(curr_bbox)

    if prev_area == 0:
        return "unknown"

    change = (curr_area - prev_area) / prev_area

    if change > threshold:
        return "approaching"
    elif change < -threshold:
        return "receding"
    else:
        return "stationary"
