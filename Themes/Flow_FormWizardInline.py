import sys, time

class FlowFormWizardInline:
    def __init__(self): self.steps=["Region","Plan","Confirm"]
    def _p(self,s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self,secs=3):
        t0=time.time()
        for s in self.steps:
            self._p(f"{s}: value ✓  (Enter to continue)"); time.sleep(secs/len(self.steps))
        self._p("\nFlowFormWizardInline done\n")

# back-compat
FormWizardInline = FlowFormWizardInline
