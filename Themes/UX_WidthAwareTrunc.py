import sys, time, shutil

class UXWidthAwareTrunc:
    def __init__(self):
        self.width = shutil.get_terminal_size((80, 20)).columns

    def _p(self, s):
        sys.stdout.write("\r\x1b[2K" + s[: self.width])
        sys.stdout.flush()

    def _short(self, name, maxw):
        if len(name) <= maxw:
            return name
        head = max(3, int(maxw * 0.6))
        tail = max(3, maxw - head - 3)
        return name[:head] + "…" + name[-tail:]

    def demo(self, secs=5):
        samples = [
            "/var/log/super/long/path/to/file/alpha_beta_gamma_delta.tar.gz",
            "/usr/share/doc/reallyreallylongfilename.txt",
            "C:\\ProgramData\\Company\\Logs\\Service_2025_10_15.log",
        ]
        t0 = time.time()
        i = 0
        while time.time() - t0 < secs:
            i = (i + 1) % len(samples)
            for _ in range(4):
                nm = self._short(samples[i], max(20, self.width - 15))
                self._p(f"name: {nm}")
                time.sleep(0.25)
        self._p("\ntruncation preview ✓\n")

# back-compat
WidthAwareTrunc = UXWidthAwareTrunc
