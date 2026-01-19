# core/risk.py

def assess_risk(object_name, distance_m):
    if distance_m is None:
        return "unknown"

    if object_name in ["car", "bus", "truck", "motorcycle"]:
        if distance_m < 5:
            return "high"
        elif distance_m < 10:
            return "medium"
        else:
            return "low"

    if object_name in ["person", "bicycle"]:
        if distance_m < 3:
            return "medium"
        else:
            return "low"

    return "low"
