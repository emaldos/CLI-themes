import sys,time
class UXTicker:
    def __init__(self):self.seq=[("starting","ok"),("checking","pass"),("sync","done"),("cleanup","done")]
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def demo(self):
        for st,res in self.seq:
            t=time.time()+1.8
            while time.time()<t:
                self._p(st+" …");time.sleep(0.12)
            self._p(st+" → "+res+"\n");time.sleep(0.2)
        self._p("complete\n")
