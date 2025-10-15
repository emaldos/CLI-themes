import sys,time,random
class NetThroughput:
    def __init__(self,width=80):self.w=width;self.hist=[]
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def _spark(self,val):self.hist=(self.hist+[(val)])[-20:];chars="▁▂▃▄▅▆▇█";mx=max(self.hist) if self.hist else 1.0;return "".join(chars[min(int((v/mx)*7),7)] for v in self.hist).ljust(20)
    def demo(self,secs=6.0):
        t0=time.time();up=0;down=0
        while time.time()-t0<secs:
            u=random.randint(30_000,200_000);d=random.randint(80_000,600_000);up+=u;down+=d;lat=random.uniform(10,90)
            self._p(f"↑{u/1024:5.1f}KB/s ↓{d/1024:5.1f}KB/s  total:{(up+down)/1024/1024:5.2f}MB  rtt:{lat:4.1f}ms {self._spark(lat)}");time.sleep(0.12)
        self._p(f"avg ↑{(up/(time.time()-t0))/1024:5.1f}KB/s ↓{(down/(time.time()-t0))/1024:5.1f}KB/s total:{(up+down)/1024/1024:5.2f}MB\n")
