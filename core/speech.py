# core/speech.py

def generate_message(primary, motion=None):
    obj = primary.get("object", "object")
    dist = primary.get("distance_m")
    risk = primary.get("risk", "unknown")

    if dist is None:
        return f"Notice. {obj} detected at an unknown distance."

    if dist < 1.0:
        return f"Warning. {obj} extremely close at {dist} meters."

    if dist < 3.0:
        return f"Warning. {obj} very close at {dist} meters."

    return f"Notice. {obj} detected {dist} meters ahead."
