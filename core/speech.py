"""
Text-to-speech module for AI Eyes.
"""

def generate_message(result):
    obj = result["object"]
    risk = result["risk"]
    distance = result["distance_m"]

    if distance is None:
        return f"{obj} ahead. Risk {risk}."

    return f"{obj} {round(distance, 1)} metres ahead. Risk {risk}."
