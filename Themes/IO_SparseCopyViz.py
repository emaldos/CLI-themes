import sys, time, random

class IOSparseCopyViz:
    def __init__(self, width=30): self.w = width; self.pos = 0
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time()
        while time.time() - t0 < secs:
            block = ["·"] * self.w
            for _ in range(random.randint(2, 5)):
                start = random.randint(0, self.w-3); end = min(self.w, start + random.randint(1, 4))
                for i in range(start, end): block[i] = "#"
            self._p("".join(block)); time.sleep(0.25)
        self._p("\nregions copied ✓\n")

# back-compat
SparseCopyViz = IOSparseCopyViz
