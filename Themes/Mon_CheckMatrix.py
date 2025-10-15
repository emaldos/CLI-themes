import sys,time,random
class MonCheckMatrix:
    def __init__(self,rows=None,cols=8):self.rows=rows or ["db","cache","api","auth","mq"];self.cols=cols
    def _up(self,n):sys.stdout.write(f"\x1b[{n}A")
    def _clr(self):sys.stdout.write("\r\x1b[2K")
    def demo(self):
        grid=[["·"]*self.cols for _ in self.rows]
        for r in range(len(self.rows)):
            self._clr();sys.stdout.write(f"{self.rows[r]:<6}"+" ".join(grid[r])+"\n")
        sys.stdout.flush()
        for c in range(self.cols):
            self._up(len(self.rows))
            for r in range(len(self.rows)):
                res=random.random()
                grid[r][c]="✓" if res>0.15 else "•" if res>0.05 else "✖"
                self._clr();sys.stdout.write(f"{self.rows[r]:<6}"+" ".join(grid[r])+"\n")
            sys.stdout.flush();time.sleep(0.5)
