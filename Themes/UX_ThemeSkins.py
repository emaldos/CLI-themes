import sys, time
class UXThemeSkins:
    def __init__(self,skins=None): self.skins=skins or ["ASCII","Minimal","Emoji-Lite","No-Color"]
    def _p(self,s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self,secs=5):
        t0=time.time(); i=0
        while time.time()-t0<secs:
            i=(i+1)%len(self.skins)
            self._p(f"skin: {self.skins[i]}  elapsed {time.time()-t0:0.1f}s"); time.sleep(0.3)
        self._p("skins cycled ✓\n")
# back-compat
ThemeSkins = UXThemeSkins
