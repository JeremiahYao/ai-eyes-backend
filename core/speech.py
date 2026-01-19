def generate_message(result):
    obj = result.get("object") or "object"
    dist = result.get("distance_m")
    motion = result.get("motion", "unknown")

    if dist is None:
        return f"Notice. {obj} detected at an unknown distance."
    elif dist < 5:
        return f"Warning. {obj} very close at {dist:.1f} meters."
    else:
        return f"Notice. {obj} detected at {dist:.1f} meters."
