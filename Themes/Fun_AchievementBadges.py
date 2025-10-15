import sys, time

class FunAchievementBadges:
    def __init__(self): self.badges = ["First Run", "100 Files", "No Errors", "Fast Build"]
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time(); i = 0
        while time.time() - t0 < secs:
            i = (i + 1) % len(self.badges)
            self._p(f"🏅 {self.badges[i]}"); time.sleep(0.4)
        self._p("\nawards shown ✓\n")

# back-compat
AchievementBadges = FunAchievementBadges
