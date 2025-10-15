import sys,time,random
class NetHealthGrid:
    def __init__(self,services=None):self.s=services or ["DB","Cache","API","Auth","MQ","Search"]
    def _up(self,n):sys.stdout.write(f"\x1b[{n}A")
    def _clr(self):sys.stdout.write("\r\x1b[2K")
    def demo(self,cycles=30):
        rows=[f"{n:<8}[ ]  0ms" for n in self.s]
        for r in rows:self._clr();sys.stdout.write(r+"\n");sys.stdout.flush()
        for _ in range(cycles):
            self._up(len(self.s))
            for n in self.s:
                ms=int(random.uniform(8,180));st="G" if ms<80 else "Y" if ms<140 else "R"
                self._clr();sys.stdout.write(f"{n:<8}[{st}] {ms:>3}ms\n");sys.stdout.flush();time.sleep(0.03)
