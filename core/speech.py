"""
Speech generation logic.
Converts pipeline results into user-friendly messages.
"""

def generate_message(r):
    obj = r.get("object", "object")
    direction = r.get("direction", "ahead")
    bucket = r.get("distance_bucket", "unknown")
    risk = r.get("risk", "unknown")

    # High risk overrides everything
    if risk == "high":
        if bucket == "near":
            return f"Warning. {obj} very close on the {direction}."
        return f"Warning. {obj} on the {direction}."

    if risk == "medium":
        return f"Caution. {obj} on the {direction}."

    # Low / unknown risk
    if bucket != "unknown":
        return f"Notice. {obj} {bucket} on the {direction}."

    return f"Notice. {obj} on the {direction}."
