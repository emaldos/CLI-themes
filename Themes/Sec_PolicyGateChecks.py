import sys, time

class SecPolicyGateChecks:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K" + s); sys.stdout.flush()
    def demo(self, secs=3):
        t = time.time()
        while time.time() - t < secs:
            self._p(f"SecPolicyGateChecks demo… {time.time() - t:0.1f}s")
            time.sleep(0.07)
        self._p("SecPolicyGateChecks done\n")

# back-compat alias
PolicyGateChecks = SecPolicyGateChecks
