OBJECT_WEIGHTS = {
    "person": 1.0,
    "car": 1.5,
    "bus": 1.7,
    "bicycle": 1.2
}

def compute_risk(distance_m, confidence, class_name):
    weight = OBJECT_WEIGHTS.get(class_name, 0.5)
    if distance_m is None:
        return 0
    return (1 / distance_m) * confidence * weight
