# core/decision.py

PRIORITY = [
    "person",
    "bicycle",
    "motorcycle",
    "car",
    "bus",
    "truck",
    "traffic light"
]

def choose_primary_threat(results):
    """
    Choose the most important object to alert on.
    """
    if not results:
        return None

    # Keep only objects we care about
    filtered = [
        r for r in results
        if r.get("object") in PRIORITY
    ]

    if not filtered:
        return None

    def sort_key(r):
        obj_priority = PRIORITY.index(r["object"])
        distance = r["distance_m"]
        return (
            obj_priority,
            distance if distance is not None else float("inf")
        )

    filtered.sort(key=sort_key)
    return filtered[0]
