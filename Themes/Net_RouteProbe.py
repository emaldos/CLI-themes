import sys, time

class NetRouteProbe:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        hops = ["local", "gateway", "isp", "edge", "origin"]
        t0 = time.time()
        for h in hops:
            self._p(f"{h} ✓  {time.time()-t0:0.1f}s"); time.sleep(secs/len(hops))
        self._p("\nroute probe complete ✓\n")

# back-compat
RouteProbe = NetRouteProbe
