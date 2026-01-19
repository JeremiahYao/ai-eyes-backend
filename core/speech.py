"""
Speech / user feedback generation logic.
Converts perception + risk data into human-readable messages.
"""

def generate_message(result):
    """
    result example:
    {
        "object": "person",
        "confidence": 0.83,
        "distance_m": 4.2,
        "risk": "medium"
    }
    """

    obj = result.get("object", "object")
    distance = result.get("distance_m")
    risk = result.get("risk", "unknown")

    if distance is None:
        distance_text = "at an unknown distance"
    else:
        distance_text = f"{distance:.1f} meters away"

    if risk == "high":
        prefix = "Warning!"
    elif risk == "medium":
        prefix = "Caution."
    else:
        prefix = "Notice."

    return f"{prefix} {obj} detected {distance_text}."

