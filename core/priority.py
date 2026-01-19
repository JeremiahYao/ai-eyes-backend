PRIORITY_CLASSES = ["person", "car", "truck", "bus", "bicycle"]

def filter_priority(results, max_items=3):
    """
    Keep only high-priority objects and limit count
    """
    filtered = []

    for r in results:
        if r["object"] in PRIORITY_CLASSES:
            filtered.append(r)

    return filtered[:max_items]
