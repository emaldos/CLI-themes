import sys,time,random
class InstallerStyle4:
    def __init__(self): self.spin="|/-\\"
    def _line(self,msg): sys.stdout.write("\r\x1b[2K"+msg); sys.stdout.flush()
    def run(self,steps):
        for name in steps:
            t0=time.time(); dur=random.uniform(1.2,3.2); i=0
            while time.time()-t0<dur:
                i=(i+1)%len(self.spin)
                self._line(f" {self.spin[i]} {name}… {time.time()-t0:0.1f}s"); time.sleep(0.06)
            self._line(f" ✓ {name} (in {time.time()-t0:0.2f}s)\n"); sys.stdout.flush()
    def demo(self):
        self.run(["update-apt","install-git","pip-rich","pull-redis","configure","verify"])
