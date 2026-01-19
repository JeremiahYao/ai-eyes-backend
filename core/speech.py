"""
Speech generation logic.
Converts pipeline results into spoken messages.
"""

def generate_message(result):
    obj = result["object"]
    distance = result.get("distance_m")
    risk = result.get("risk", "unknown")

    if distance is None:
        if risk == "high":
            return f"Warning. {obj} detected nearby. Distance unknown."
        elif risk == "medium":
            return f"Caution. {obj} detected. Distance unknown."
        else:
            return f"Notice. {obj} detected at an unknown distance."

    # Distance is known
    distance = round(distance, 1)

    if risk == "high":
        return f"Warning. {obj} detected {distance} meters ahead."
    elif risk == "medium":
        return f"Caution. {obj} detected {distance} meters away."
    else:
        return f"{obj} detected {distance} meters ahead."
