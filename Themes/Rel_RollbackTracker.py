import sys, time

class RelRollbackTracker:
    def __init__(self): pass
    def _p(self, s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self, secs=3):
        steps = ["stop", "undo-migrate", "restore-backup", "start", "verify"]
        t0 = time.time()
        for s in steps:
            self._p(f"rollback: {s} … {time.time()-t0:0.1f}s"); time.sleep(secs/len(steps))
        self._p("\nrollback complete ✓\n")

# back-compat
RollbackTracker = RelRollbackTracker
