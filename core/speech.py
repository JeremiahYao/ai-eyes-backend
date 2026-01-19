"""
Speech / message generation logic.
Converts pipeline results into human-readable messages.
"""

def generate_message(result):
    object_name = result["object"]
    distance = result["distance_m"]
    risk = result["risk"]

    # Distance phrase
    if distance is None:
        distance_text = "at an unknown distance"
    else:
        distance_text = f"{distance:.1f} meters ahead"

    # Risk-based phrasing
    if risk == "high":
        prefix = "⚠️ Warning!"
    elif risk == "medium":
        prefix = "Caution:"
    else:
        prefix = "Info:"

    message = f"{prefix} {object_name.capitalize()} detected {distance_text}. Risk level: {risk}."

    return message
