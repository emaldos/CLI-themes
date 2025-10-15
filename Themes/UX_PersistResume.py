import sys, time, json, os, tempfile
class UXPersistResume:
    def __init__(self, fname=None): self.fname=fname or os.path.join(tempfile.gettempdir(),"cli_themes.progress.json")
    def _p(self,s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def _save(self,step): json.dump({"step":step,"ts":time.time()}, open(self.fname,"w"))
    def demo(self,secs=4):
        t0=time.time(); step=0
        while time.time()-t0<secs:
            step+=1; self._save(step); self._p(f"progress step={step} saved → {os.path.basename(self.fname)}"); time.sleep(0.4)
        self._p("\nresume token written ✓\n")
# back-compat
PersistResume = UXPersistResume
