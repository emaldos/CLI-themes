import sys,time,random
class InstallerStyle5:
    def __init__(self,width=80): self.width=width
    def _pad(self,left,right):
        dots=max(2,self.width-len(left)-len(right)); return left+("."*dots)+right
    def run(self,steps,fail_rate=0.0):
        for name in steps:
            left=f"Processing {name}"
            t0=time.time(); dur=random.uniform(0.8,2.0)
            while time.time()-t0<dur:
                msg=self._pad(left,f"{time.time()-t0:0.1f}s")
                sys.stdout.write("\r\x1b[2K"+msg); sys.stdout.flush(); time.sleep(0.05)
            ok = random.random()>=fail_rate
            right="[OK]" if ok else "[FAIL]"
            sys.stdout.write("\r\x1b[2K"+self._pad(left,right)+"\n"); sys.stdout.flush()
    def demo(self):
        self.run(["repos","python3-pip","git","docker.io","compose","cleanup"],fail_rate=0.0)
