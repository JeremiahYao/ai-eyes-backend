# core/memory.py

class TemporalMemory:
    def __init__(self, cooldown_frames=5, distance_threshold=0.5):
        self.last_object = None
        self.last_distance = None
        self.cooldown = 0
        self.cooldown_frames = cooldown_frames
        self.distance_threshold = distance_threshold

    def analyze(self, current):
        """
        Returns: (should_alert, motion)
        motion = 'approaching', 'receding', or None
        """
        if current is None:
            self.last_object = None
            self.last_distance = None
            self.cooldown = 0
            return False, None

        motion = None

        if (
            self.last_object == current["object"]
            and self.last_distance is not None
            and current["distance_m"] is not None
        ):
            delta = self.last_distance - current["distance_m"]
            if abs(delta) > self.distance_threshold:
                motion = "approaching" if delta > 0 else "receding"

        if self.cooldown > 0:
            self.cooldown -= 1
            alert = False
        else:
            alert = True
            self.cooldown = self.cooldown_frames

        self.last_object = current["object"]
        self.last_distance = current["distance_m"]

        return alert, motion
