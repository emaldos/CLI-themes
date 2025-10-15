import sys,time,random
class MonLogTail:
    def __init__(self,lines=6):self.n=lines
    def _up(self,n):sys.stdout.write(f"\x1b[{n}A")
    def _clr(self):sys.stdout.write("\r\x1b[2K")
    def demo(self,secs=7):
        head=f"CPU:{random.uniform(2,8):4.1f}% RAM:{random.uniform(20,45):4.1f}% errs:0"
        sys.stdout.write(head+"\n");sys.stdout.flush()
        buf=[]
        t0=time.time()
        while time.time()-t0<secs:
            if random.random()<0.2:head=f"CPU:{random.uniform(2,35):4.1f}% RAM:{random.uniform(20,55):4.1f}% errs:{random.randint(0,2)}"
            buf.append(f"{time.strftime('%H:%M:%S')} INFO line {len(buf)+1}")
            buf=buf[-self.n:]
            self._up(self.n);self._clr();sys.stdout.write(head+"\n");sys.stdout.flush()
            for i in range(self.n):
                self._clr();sys.stdout.write((buf[i] if i<len(buf) else "")+"\n")
            sys.stdout.flush();time.sleep(0.25)
