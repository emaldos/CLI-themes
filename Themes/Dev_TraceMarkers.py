import sys, time

class DevTraceMarkers:
    def __init__(self): self.seq=["INIT","SETUP","RUN","TEARDOWN"]
    def _p(self,s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self,secs=3):
        t0=time.time()
        for tag in self.seq:
            self._p(f"[TRACE] {int(time.time()*1000)} :: {tag}"); time.sleep(secs/len(self.seq))
        self._p("\nDevTraceMarkers done\n")

# back-compat
TraceMarkers = DevTraceMarkers
