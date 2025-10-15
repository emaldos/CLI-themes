import sys, time, random, math

class VisFunnel:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t=time.time()
        while time.time()-t<secs:
            self._p(f"VisFunnel demo… {time.time()-t:0.1f}s"); time.sleep(0.07)
        self._p("VisFunnel done\n")

# Back-compat alias
Funnel = VisFunnel
