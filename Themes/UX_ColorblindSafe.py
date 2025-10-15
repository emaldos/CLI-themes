import sys, time
class UXColorblindSafe:
    def __init__(self): self.patterns=["##","==","..","++","**"]
    def _p(self,s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self,secs=4):
        t0=time.time(); i=0
        while time.time()-t0<secs:
            i=(i+1)%len(self.patterns)
            self._p(f"pattern: {self.patterns[i]}  elapsed {time.time()-t0:0.1f}s"); time.sleep(0.25)
        self._p("colorblind-safe pattern cycle ✓\n")
# back-compat
ColorblindSafe = UXColorblindSafe
