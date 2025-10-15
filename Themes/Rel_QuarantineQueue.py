import sys, time, random

class RelQuarantineQueue:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time(); quarantined = 0
        while time.time() - t0 < secs:
            if random.random() < 0.5: quarantined += 1
            self._p(f"quarantine: {quarantined}  (press Enter later to replay)")
            time.sleep(0.15)
        self._p("\nreplayed quarantined items ✓\n")

# back-compat
QuarantineQueue = RelQuarantineQueue
