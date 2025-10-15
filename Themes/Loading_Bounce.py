import sys,time
class LoaderBounce:
    def __init__(self,width=40):self.w=max(8,width)
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def run(self,label="processing",secs=5.0):
        t0=time.time();pos=0;dir=1
        while time.time()-t0<secs:
            bar=[" "]*self.w;bar[pos]="=";self._p(f"{label:<12}[{''.join(bar)}] {time.time()-t0:0.1f}s");time.sleep(0.02);pos+=dir
            if pos<=0 or pos>=self.w-1:dir*=-1
        self._p(f"{label:<12}[{'='*(self.w)}] done in {time.time()-t0:0.2f}s\n")
    def demo(self):
        self.run("bouncing",secs=6)
