# core/motion.py

"""
Simple motion analysis across frames.
(Currently defaults to stationary — safe placeholder)
"""

_previous_bboxes = {}


def analyze_motion(results):
    """
    Adds a 'motion' field to each detection.
    Currently assumes stationary (placeholder logic).
    """

    global _previous_bboxes

    for r in results:
        obj = r.get("object")
        bbox = r.get("bbox")

        if bbox is None:
            r["motion"] = "unknown"
            continue

        # Placeholder logic
        r["motion"] = "stationary"

        # Store for future frames
        _previous_bboxes[obj] = bbox

    return results
