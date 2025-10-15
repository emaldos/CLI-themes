import sys,time,random,threading
from dataclasses import dataclass
from typing import List
@dataclass
class _Svc:name:str;state:str="Pulling";t0:float=0.0;dur:float=0.0;done:bool=False
class InstallerStyle1:
    def __init__(self,services:List[str],parallel:int=3,total:int=None,interval:float=0.1):
        self.rows=[_Svc(s) for s in services];self.parallel=parallel;self.interval=interval;self.total=total or len(self.rows)
    def _fmt_t(self,s):return f"{s:>5.1f}s"
    def _tick(self,svc:_Svc):
        svc.t0=time.time();svc.dur=random.uniform(2.5,7.5);time.sleep(svc.dur);svc.done=True;svc.state="Pulled"
    def run(self):
        start=time.time();active=[]
        while True:
            for s in self.rows:
                if not s.done and s.t0==0 and sum(1 for a in active if a.is_alive())<self.parallel:
                    s.state="Pulling";t=threading.Thread(target=self._tick,args=(s,),daemon=True);t.start();active.append(t)
            lines=[]
            for s in self.rows:
                t=time.time()-s.t0 if s.t0 else time.time()-start
                mark="✓" if s.done else "∙"
                lines.append(f"{mark} {s.name:<18}{s.state:<8}{self._fmt_t(t)}")
            sys.stdout.write("\x1b[1J\x1b[H");sys.stdout.write(f"[+] Running {sum(1 for s in self.rows if s.done)}/{self.total}\n");sys.stdout.write("\n".join(lines)+"\n");sys.stdout.flush()
            if all(s.done for s in self.rows):break
            time.sleep(self.interval)
