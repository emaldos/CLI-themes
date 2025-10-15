import sys, time

class VisCountdownGate:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time()
        while True:
            elapsed = time.time() - t0
            if elapsed >= secs: break
            left = secs - elapsed
            self._p(f"Countdown in {left:0.1f}s…")
            time.sleep(0.07)
        self._p("Gate opened ✓\n")

# Back-compat alias
CountdownGate = VisCountdownGate
