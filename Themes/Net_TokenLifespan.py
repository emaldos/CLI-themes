import sys, time

class NetTokenLifespan:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time(); ttl = secs
        while True:
            left = ttl - (time.time()-t0)
            if left <= 0: break
            self._p(f"token refresh in {left:0.1f}s"); time.sleep(0.1)
        self._p("token refreshed ✓\n")

# back-compat
TokenLifespan = NetTokenLifespan
