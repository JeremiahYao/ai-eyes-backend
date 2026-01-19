# core/decision.py

PRIORITY_ORDER = {
    "person": 3,
    "bicycle": 3,
    "car": 2,
    "bus": 2,
    "truck": 2,
    "motorcycle": 2,
    "traffic light": 1
}

def choose_primary_threat(results):
    """
    Choose the most important object even if
    distance and risk are unknown.
    """

    if not results:
        return None

    best = None
    best_score = -1

    for r in results:
        label = r.get("object")
        confidence = r.get("confidence", 0)

        base_score = PRIORITY_ORDER.get(label, 0)
        score = base_score + confidence

        if score > best_score:
            best = r
            best_score = score

    return best
