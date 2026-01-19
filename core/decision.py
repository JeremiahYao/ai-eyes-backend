IMPORTANT_OBJECTS = {
    "person", "car", "bus", "truck", "bicycle", "motorcycle"
}

def choose_primary_threat(results):
    if not results:
        return None

    filtered = [
        r for r in results
        if r.get("object") in IMPORTANT_OBJECTS
    ]

    if not filtered:
        return None

    # Prefer closest known distance
    filtered.sort(
        key=lambda r: (
            r["distance_m"] is None,
            r["distance_m"] if r["distance_m"] else float("inf")
        )
    )

    return filtered[0]
