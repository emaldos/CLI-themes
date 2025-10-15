import sys, time

class MonServiceTimeline:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        stages = ["start", "init", "ready"]
        t0 = time.time()
        for s in stages:
            self._p(f"{s:<5} |{'='*(stages.index(s)+1)}>{' '*(len(stages)-stages.index(s)-1)}| {time.time()-t0:0.1f}s")
            time.sleep(secs/len(stages))
        self._p("\nservice timeline complete ✓\n")

# back-compat
ServiceTimeline = MonServiceTimeline
