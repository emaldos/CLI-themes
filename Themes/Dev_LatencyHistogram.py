import sys, time, random

class DevLatencyHistogram:
    def __init__(self): self.buckets=[0]*10
    def _p(self,s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self,secs=3):
        t0=time.time()
        while time.time()-t0<secs:
            v=random.random()**2  # more small latencies
            idx=min(int(v*len(self.buckets)),len(self.buckets)-1)
            self.buckets[idx]+=1
            bar="".join("#"*(b>0) for b in self.buckets)
            self._p(f"latency hist: {bar}"); time.sleep(0.08)
        self._p("\nDevLatencyHistogram done\n")

# back-compat
LatencyHistogram = DevLatencyHistogram
