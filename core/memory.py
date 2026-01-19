# core/memory.py

class TemporalMemory:
    def __init__(self, cooldown_frames=5):
        self.last_object = None
        self.cooldown = 0
        self.cooldown_frames = cooldown_frames

    def should_alert(self, current_object):
        """
        Decide whether to speak based on recent history.
        """
        if current_object is None:
            self.last_object = None
            self.cooldown = 0
            return False

        if self.cooldown > 0 and current_object["object"] == self.last_object:
            self.cooldown -= 1
            return False

        self.last_object = current_object["object"]
        self.cooldown = self.cooldown_frames
        return True
