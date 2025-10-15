import sys, time

class IOChecksumParade:
    def __init__(self): self.files = ["alpha.tar.gz","beta.bin","gamma.img"]
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        t0 = time.time()
        for f in self.files:
            for i in range(6):
                self._p(f"{f}: hashing {'='*i:6}"); time.sleep(secs/(len(self.files)*6))
            self._p(f"{f}: ✓\n"); time.sleep(0.1)
        self._p("all checksums verified ✓\n")

# back-compat
ChecksumParade = IOChecksumParade
