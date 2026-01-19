"""
Stereo distance estimation using disparity.
"""

def estimate_distance(x_left, x_right, focal_length_px, baseline_m):
    """
    Returns distance in meters or None.
    """
    disparity = abs(x_left - x_right)

    if disparity < 1e-6:
        return None

    return (focal_length_px * baseline_m) / disparity
