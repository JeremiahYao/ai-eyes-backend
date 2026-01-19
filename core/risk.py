"""
Risk assessment logic for AI Eyes.

Determines how dangerous an object is
based on object type and estimated distance.
"""

def assess_risk(object_name, distance_m):
    """
    object_name: string (e.g. 'car', 'person')
    distance_m: float or None
    returns: 'high', 'medium', 'low', or 'unknown'
    """

    # If distance cannot be estimated
    if distance_m is None:
        return "unknown"

    # Vehicles are high-risk objects
    if object_name in ["car", "bus", "truck", "motorcycle"]:
        if distance_m < 5:
            return "high"
        elif distance_m < 10:
            return "medium"
        else:
            return "low"

    # Humans & bicycles
    if object_name in ["person", "bicycle"]:
        if distance_m < 3:
            return "medium"
        else:
            return "low"

    # Default for everything else
    return "low"
