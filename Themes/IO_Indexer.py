import sys,time,random
class IOIndexer:
    def __init__(self):pass
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def demo(self,secs=6):
        t0=time.time();sc=0;ix=0;sk=0
        while time.time()-t0<secs:
            sc+=random.randint(80,150);n=random.randint(60,120);ix+=n;sk+=random.randint(0,5);rate=n/0.12
            self._p(f"scanned:{sc:6d} indexed:{ix:6d} skipped:{sk:4d} rate:{rate/1000:4.1f}k/s");time.sleep(0.12)
        self._p(f"done scanned:{sc} indexed:{ix} skipped:{sk}\n")
