import sys,time,random
class IOExtractor:
    def __init__(self,width=26):self.w=width
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def _bar(self,p):f=int(self.w*p);return "["+"="*f+">"+" "*(self.w-f-1)+"]"
    def demo(self,files=180):
        phases=[("scan",0.3),("deflate",0.35),("untar",0.35)]
        done=0;start=time.time()
        for name,share in phases:
            t=time.time();dur=share*6
            while time.time()-t<dur:
                p=(time.time()-t)/dur;rate=random.uniform(8,40);done=min(files,int((sum(s for _,s in phases[:phases.index((name,share))])+p*share)*files))
                self._p(f"{name:<8}{self._bar(p)} {done}/{files} files {rate:4.1f} MB/s {(time.time()-start):0.1f}s");time.sleep(0.06)
        self._p(f"done     [{'='*self.w}] {files}/{files} files {(time.time()-start):0.1f}s\n")
