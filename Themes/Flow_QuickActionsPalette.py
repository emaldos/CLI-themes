import sys, time

class FlowQuickActionsPalette:
    def __init__(self): self.actions = [":retry", ":logs", ":verbose", ":quit"]
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time(); i = 0
        while time.time() - t0 < secs:
            i = (i + 1) % len(self.actions)
            self._p(f"Palette {self.actions[i]}  (type ':' to open)  {time.time()-t0:0.1f}s")
            time.sleep(0.25)
        self._p("\npalette closed ✓\n")

# back-compat
QuickActionsPalette = FlowQuickActionsPalette
