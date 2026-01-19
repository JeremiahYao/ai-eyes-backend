# core/decision.py

"""
Decision logic for choosing the primary object to alert the user about.
"""

IMPORTANT_OBJECTS = {
    "car",
    "bus",
    "truck",
    "motorcycle",
    "person",
    "bicycle"
}

RISK_PRIORITY = {
    "high": 3,
    "medium": 2,
    "unknown": 1,
    "low": 0
}


def choose_primary_threat(results):
    """
    Select the most important object from pipeline results.

    Args:
        results (list[dict]): Output from navigation pipeline

    Returns:
        dict | None: The chosen object, or None if nothing relevant
    """

    if not results:
        return None

    # Keep only objects we care about
    candidates = [
        r for r in results
        if r.get("object") in IMPORTANT_OBJECTS
    ]

    if not candidates:
        return None

    # Sort by risk priority, then confidence
    candidates.sort(
        key=lambda r: (
            RISK_PRIORITY.get(r.get("risk", "low"), 0),
            r.get("confidence", 0.0)
        ),
        reverse=True
    )

    return candidates[0]
