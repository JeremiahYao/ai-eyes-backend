# core/speech.py

def generate_message(result):
    obj = result.get("object", "object")
    risk = result.get("risk", "unknown")
    distance = result.get("distance_m")

    if distance is None:
        return f"Notice. {obj} detected at an unknown distance."

    if risk == "high":
        return f"Warning! {obj} very close. Please stop."
    elif risk == "medium":
        return f"Caution. {obj} nearby."
    else:
        return f"Notice. {obj} detected at {distance:.1f} meters."
