import sys,time,random,threading
class InstallerStyle3:
    def __init__(self):self._lines=0
    def _up(self,n): 
        if n>0: sys.stdout.write(f"\x1b[{n}A")
    def _clr(self): sys.stdout.write("\r\x1b[2K")
    def _print_lines(self,rows):
        if self._lines: self._up(self._lines)
        for r in rows: self._clr(); sys.stdout.write(r+"\n")
        sys.stdout.flush(); self._lines=len(rows)
    def run(self,steps):
        rows=[f"∙ {name:<22}… 0.0s" for name in steps];t0=[0]*len(steps);done=[False]*len(steps)
        ts=[]
        for i,name in enumerate(steps):
            d=random.uniform(1.5,4.5); t0[i]=time.time()
            thr=threading.Thread(target=lambda idx=i,dd=d:(time.sleep(dd),ts.append(idx)),daemon=True);thr.start()
        while len(ts)<len(steps):
            for i,name in enumerate(steps):
                if done[i]: continue
                el=time.time()-t0[i] if t0[i] else 0
                rows[i]=f"∙ {name:<22}… {el:0.1f}s"
            self._print_lines(rows); time.sleep(0.05)
            while ts:
                j=ts.pop(0); done[j]=True
                rows[j]=f"✓ {steps[j]:<22}done {time.time()-t0[j]:0.1f}s"
                self._print_lines(rows)
        self._print_lines(rows)
    def demo(self):
        self.run(["prepare-env","install-deps","pull-images","migrate-db","seed-data","start-services"])
