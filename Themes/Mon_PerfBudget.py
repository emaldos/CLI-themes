import sys, time

class MonPerfBudget:
    def __init__(self, budget=6.0): self.budget = budget
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        left = self.budget; t0 = time.time()
        steps = ["fetch","process","write"]
        for s in steps:
            spent = secs/len(steps); left -= spent
            self._p(f"{s:<8} budget left: {max(0,left):0.1f}s"); time.sleep(spent)
        self._p("\nperf budget run complete ✓\n")

# back-compat
PerfBudget = MonPerfBudget
