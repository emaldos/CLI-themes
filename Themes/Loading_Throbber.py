import sys,time,random
class LoaderThrobber:
    def __init__(self):self.spin="|/-\\"
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def run(self,status,secs=5.0):
        i=0;t0=time.time();idx=0
        while time.time()-t0<secs:
            i=(i+1)%len(self.spin);idx=(idx+1)%len(status)
            self._p(f" {self.spin[i]} {status[idx]}… {time.time()-t0:0.1f}s");time.sleep(0.07)
        self._p(f" ✓ {status[idx]} (in {time.time()-t0:0.2f}s)\n")
    def demo(self):
        self.run(["parsing","linking","optimizing","finalizing"],secs=6)
