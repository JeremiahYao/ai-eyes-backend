# core/decision.py

IMPORTANT_OBJECTS = {
    "car", "bus", "truck", "motorcycle", "person", "bicycle"
}

RISK_PRIORITY = {
    "high": 3,
    "medium": 2,
    "unknown": 1,
    "low": 0
}


def choose_primary_threat(results):
    if not results:
        return None

    candidates = [
        r for r in results
        if r.get("object") in IMPORTANT_OBJECTS
    ]

    if not candidates:
        return None

    candidates.sort(
        key=lambda r: (
            RISK_PRIORITY.get(r.get("risk", "low"), 0),
            r.get("motion") != "stationary",
            r.get("confidence", 0.0)
        ),
        reverse=True
    )

    return candidates[0]
