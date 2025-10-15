import sys,time
class UXEmojiLite:
    def __init__(self):self.frames=["⏳","🔄","🌀","⚙️","🔗"];self.ok="✅"
    def _p(self,s):sys.stdout.write("\r\x1b[2K"+s);sys.stdout.flush()
    def demo(self,secs=5):
        t0=time.time();i=0
        while time.time()-t0<secs:
            i=(i+1)%len(self.frames);self._p(f"{self.frames[i]} working… {time.time()-t0:0.1f}s");time.sleep(0.12)
        self._p(self.ok+" done\n")
