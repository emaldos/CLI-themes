import sys,time,random
class MonHeartbeat:
    def __init__(self):pass
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def demo(self,beats=8):
        for i in range(beats):
            ok=random.random()>0.1;st="OK" if ok else "WARN"
            self._p(f"[♥] {time.strftime('%H:%M:%S')} {st}");time.sleep(0.8)
        self._p(f"[♥] done\n")
