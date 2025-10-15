import sys, time

class FlowYesNoTimeout:
    def __init__(self, default="yes", timeout=5):
        self.default = default; self.timeout = timeout
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time()
        while time.time() - t0 < secs:
            left = max(0, self.timeout - int(time.time() - t0))
            self._p(f"Proceed? (Y/n) auto-{self.default} in {left}s"); time.sleep(0.25)
        self._p(f"\nSelected: {self.default}\n")

# back-compat
YesNoTimeout = FlowYesNoTimeout
