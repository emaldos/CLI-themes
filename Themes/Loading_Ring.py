import sys,time
class LoaderRing:
    def __init__(self,ascii_only=True):self.frames=["(-)","(\\)","(|)","(/)"] if ascii_only else ["◴","◷","◶","◵"]
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def run(self,label="compute",secs=5.0):
        i=0;t0=time.time()
        while time.time()-t0<secs:
            i=(i+1)%len(self.frames);self._p(f" {self.frames[i]} {label}… {time.time()-t0:0.1f}s");time.sleep(0.07)
        self._p(f" ✓ {label} (in {time.time()-t0:0.2f}s)\n")
    def demo(self):
        self.run("ring",secs=6)
