import sys, time
class UXSoundHooks:
    def __init__(self,beep=True): self.beep=beep
    def _p(self,s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self,secs=3):
        t0=time.time()
        while time.time()-t0<secs:
            self._p(f"working… {time.time()-t0:0.1f}s"); time.sleep(0.2)
        self._p("done ✓\n"); 
        if self.beep: sys.stdout.write("\a"); sys.stdout.flush()
# back-compat
SoundHooks = UXSoundHooks
