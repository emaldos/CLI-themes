import sys,time,random
class IOSegmented:
    def __init__(self,segments=4,width=24):self.k=segments;self.w=width
    def _up(self,n):sys.stdout.write(f"\x1b[{n}A")
    def _clr(self):sys.stdout.write("\r\x1b[2K")
    def demo(self):
        bars=[0]*self.k
        for i in range(self.k):self._clr();sys.stdout.write(f"seg {i+1}/{self.k} [{' '*self.w}] 0%\n");sys.stdout.flush()
        left=self.k
        while left>0:
            self._up(self.k);left=0
            for i in range(self.k):
                if bars[i]<self.w:bars[i]+=random.randint(0,2)
                if bars[i]>self.w:bars[i]=self.w
                pct=int((bars[i]/self.w)*100)
                self._clr();sys.stdout.write(f"seg {i+1}/{self.k} [{'='*bars[i]}{'> ' if bars[i]<self.w else ''}{' '*(self.w-bars[i]- (0 if bars[i]==self.w else 2))}] {pct}%\n");sys.stdout.flush()
                if bars[i]<self.w:left+=1
            time.sleep(0.05)
        self._clr();sys.stdout.write("merging… checksum OK\n");sys.stdout.flush()
