# core/decision.py

RISK_PRIORITY = {
    "high": 3,
    "medium": 2,
    "low": 1,
    "unknown": 0
}

def choose_primary_threat(results):
    """
    Select the most important object to warn about.
    """
    if not results:
        return None

    results_sorted = sorted(
        results,
        key=lambda r: RISK_PRIORITY.get(r["risk"], 0),
        reverse=True
    )

    return results_sorted[0]
