"""
Simple object matching between left and right frames.
Improved later with IoU / Hungarian matching.
"""

def match_detections(detections_left, detections_right):
    """
    Matches detections by class name.
    Returns list of (left_det, right_det)
    """
    matches = []

    for dl in detections_left:
        for dr in detections_right:
            if dl["class_name"] == dr["class_name"]:
                matches.append((dl, dr))
                break

    return matches
