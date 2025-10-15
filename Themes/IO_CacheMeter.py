import sys, time, random

class IOCacheMeter:
    def __init__(self): self.cache = 0; self.net = 0
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time()
        while time.time() - t0 < secs:
            if random.random() < 0.6: self.cache += random.randint(5, 20)
            else: self.net += random.randint(5, 20)
            total = self.cache + self.net or 1
            pct = int(self.cache * 100 / total)
            self._p(f"from cache: {pct:3d}%  (cache {self.cache}, net {self.net})")
            time.sleep(0.2)
        self._p("\ncache meter complete ✓\n")

# back-compat
CacheMeter = IOCacheMeter
