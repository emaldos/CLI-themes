import sys,time,math
class LoaderWave:
    def __init__(self,width=48):self.w=width
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def run(self,label="loading",secs=5.0):
        t0=time.time()
        while time.time()-t0<secs:
            t=time.time()-t0;line=[]
            for x in range(self.w):
                y=math.sin((x/6.0)+(t*6.0))
                line.append("~" if y>0.2 else "-" if y<-0.2 else "_")
            self._p(f"{label:<12}{''.join(line)} {t:0.1f}s");time.sleep(0.05)
        self._p(f"{label:<12}{'~'*self.w} done in {time.time()-t0:0.2f}s\n")
    def demo(self):
        self.run("wave",secs=6)
