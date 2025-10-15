import sys, time, random

class RelAutoRetryLadder:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time(); attempt = 0; back = 0.5
        while time.time() - t0 < secs:
            attempt += 1
            until = time.time() + back + random.uniform(0, 0.3)
            while time.time() < until:
                self._p(f"attempt {attempt} in {(until-time.time()):0.1f}s …")
                time.sleep(0.05)
            ok = random.random() > 0.6
            if ok:
                self._p(f"connected on attempt {attempt}\n"); return
            self._p(f"attempt {attempt} failed\n"); time.sleep(0.2); back = min(4.0, back*2)

# back-compat
AutoRetryLadder = RelAutoRetryLadder
