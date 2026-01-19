# core/speech.py

def generate_message(result, motion=None):
    obj = result["object"]
    risk = result.get("risk", "unknown")
    distance = result.get("distance_m")

    if distance is None:
        base = f"{obj} detected at an unknown distance."
    else:
        base = f"{obj} detected at {distance:.1f} meters."

    if motion == "approaching":
        return f"Warning. {base} Approaching."
    if motion == "receding":
        return f"Notice. {base} Moving away."

    if risk == "high":
        return f"Warning. {base}"
    return f"Notice. {base}"
