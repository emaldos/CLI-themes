import sys,time
class NetHandshake:
    def __init__(self):self.steps=["DNS","TCP SYN","TLS","AUTH","READY"];self.mark=["∙"]*len(self.steps)
    def _up(self,n):sys.stdout.write(f"\x1b[{n}A")
    def _clr(self):sys.stdout.write("\r\x1b[2K")
    def demo(self,delay=0.6):
        rows=[f"{self.mark[i]} {s}" for i,s in enumerate(self.steps)]
        for r in rows:self._clr();sys.stdout.write(r+"\n");sys.stdout.flush()
        for i in range(len(self.steps)):
            time.sleep(delay);self._up(len(self.steps));self.mark[i]="✓";rows=[f"{self.mark[j]} {self.steps[j]}" for j in range(len(self.steps))]
            for r in rows:self._clr();sys.stdout.write(r+"\n");sys.stdout.flush()
