import sys, time

class FlowDryRunDiff:
    def __init__(self): self.items=[("create","/etc/app.conf"),("update","/var/app.bin"),("skip","/tmp/cache")]
    def _p(self,s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self,secs=3):
        for op,path in self.items:
            self._p(f"{op:<6} {path}"); time.sleep(secs/len(self.items))
        self._p("\nFlowDryRunDiff done\n")

# back-compat
DryRunDiff = FlowDryRunDiff
