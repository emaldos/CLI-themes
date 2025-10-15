import sys, time, random

class MonAlertWaterfall:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time()
        while time.time()-t0 < secs:
            sev = random.choice(["INFO","WARN","ERR"])
            self._p(f"{time.strftime('%H:%M:%S')} {sev} new event"); time.sleep(0.4)
        self._p("\nalerts quieted ✓\n")

# back-compat
AlertWaterfall = MonAlertWaterfall
