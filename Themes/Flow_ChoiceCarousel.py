import sys, time

class FlowChoiceCarousel:
    def __init__(self): self.choices=["dev","stage","prod","custom"]
    def _p(self,s): sys.stdout.write("\r\x1b[2K"+s); sys.stdout.flush()
    def demo(self,secs=3):
        t0=time.time(); i=0
        while time.time()-t0<secs:
            i=(i+1)%len(self.choices)
            self._p(f"[←/→] preset: {self.choices[i]}"); time.sleep(0.35)
        self._p("\nFlowChoiceCarousel done\n")

# back-compat
ChoiceCarousel = FlowChoiceCarousel
