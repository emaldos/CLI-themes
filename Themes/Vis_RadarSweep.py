import sys, time

class VisRadarSweep:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        frames = ["–", "\\", "|", "/"]
        t0 = time.time(); i = 0
        while time.time() - t0 < secs:
            i = (i + 1) % len(frames)
            self._p(f"Radar {frames[i]} sweeping… {time.time()-t0:0.1f}s")
            time.sleep(0.07)
        self._p("Radar sweep complete ✓\n")

# Back-compat alias
RadarSweep = VisRadarSweep
