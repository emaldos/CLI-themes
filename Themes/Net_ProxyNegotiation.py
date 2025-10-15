import sys, time

class NetProxyNegotiation:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        steps = ["Detect", "Auth", "Tunnel", "Ready"]
        t0 = time.time()
        for s in steps:
            self._p(f"{s}… {time.time()-t0:0.1f}s"); time.sleep(secs/len(steps))
        self._p("\nproxy negotiation complete ✓\n")

# back-compat
ProxyNegotiation = NetProxyNegotiation
