import sys,time,random
class NetReconnect:
    def __init__(self):pass
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def demo(self,max_attempts=5):
        back=1.0
        for i in range(1,max_attempts+1):
            until=time.time()+back+random.uniform(0,0.5)
            while True:
                rem=max(0,until-time.time());self._p(f"retry {i} in {rem:0.1f}s…");time.sleep(0.1)
                if rem<=0:break
            ok=random.random()>0.6 if i<max_attempts else True
            if ok:self._p(f"connected on attempt {i}\n");return
            self._p(f"attempt {i} failed\n");time.sleep(0.3);back=min(8.0,back*2)
