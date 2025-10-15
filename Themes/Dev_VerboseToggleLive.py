import sys, time

class DevVerboseToggleLive:
    def __init__(self): self.verbose=False
    def _p(self,s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self,secs=3):
        t0=time.time()
        while time.time()-t0<secs:
            self.verbose = not self.verbose
            msg = "detail: compiling assets…" if self.verbose else "status: working…"
            self._p(msg); time.sleep(0.4)
        self._p("\nDevVerboseToggleLive done\n")

# back-compat
VerboseToggleLive = DevVerboseToggleLive
