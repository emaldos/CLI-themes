import sys,time
class UXWizard:
    def __init__(self):self.steps=["Select region","Choose plan","Confirm settings","Apply changes"]
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def demo(self):
        for s in self.steps:
            for i in range(12):
                self._p(f"{s} (Enter to continue)");time.sleep(0.08)
            self._p(f"✓ {s}\n");time.sleep(0.3)
        self._p("Wizard complete\n")
