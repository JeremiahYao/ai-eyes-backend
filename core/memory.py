# core/memory.py

class TemporalMemory:
    def __init__(self, distance_delta=1.0):
        self.last_object = None
        self.last_distance = None
        self.distance_delta = distance_delta

    def analyze(self, primary):
        """
        Decide whether to alert based on change.
        """
        if primary is None:
            return False, None

        obj = primary["object"]
        dist = primary["distance_m"]

        # First alert ever
        if self.last_object is None:
            self.last_object = obj
            self.last_distance = dist
            return True, "new"

        # Object changed
        if obj != self.last_object:
            self.last_object = obj
            self.last_distance = dist
            return True, "changed"

        # Distance significantly changed
        if dist is not None and self.last_distance is not None:
            if abs(dist - self.last_distance) >= self.distance_delta:
                self.last_distance = dist
                return True, "approaching"

        return False, None
