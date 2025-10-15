import sys,time,random,shutil
class InstallerStyle2:
    def __init__(self,width:int=shutil.get_terminal_size((80,20)).columns):self.width=width;self._last=0
    def _fmt_size(self,b):
        u=["B","K","M","G","T"];i=0;f=float(b)
        while f>=1024 and i<len(u)-1:f/=1024;i+=1
        return f"{f:.2f}{u[i]}"
    def _fmt_speed(self,bps):
        u=["B/s","KB/s","MB/s","GB/s"];i=0;f=float(bps)
        while f>=1024 and i<len(u)-1:f/=1024;i+=1
        return f"{f:.2f}{u[i]}"
    def _print(self,s):
        pad=max(0,self._last-len(s))
        sys.stdout.write("\r"+s+(" "*pad));sys.stdout.flush();self._last=len(s)
    def _clear(self):
        if self._last: sys.stdout.write("\r"+" "*self._last+"\r");sys.stdout.flush();self._last=0
    def download(self,filename:str,size:int=24000,speed:int=0,leave:bool=False):
        t0=time.time();done=0;barw=max(10,min(40,self.width-40));spd=speed or random.uniform(120*1024,1024*1024)
        try:
            while done<size:
                dt=0.05;chunk=min(int(spd*dt),size-done);time.sleep(dt);done+=chunk
                pct=done/size;fill=int(barw*pct);bar="["+"="*fill+">"+" "*(barw-fill-1)+"]"
                left=f"{pct*100:>3.0f}%{bar}"
                right=f"{self._fmt_size(done):>8}  --.-KB/s"
                pad=self.width-2-len(filename)-len(left)-len(right);pad=max(1,pad)
                self._print(filename+" "*pad+left+" "+right)
            elapsed=time.time()-t0
            final_right=f"{self._fmt_size(done):>8}  {self._fmt_speed(done/elapsed):>8}    in {elapsed:0.3f}s"
            pad=self.width-2-len(filename)-len(left)-len(final_right);pad=max(1,pad)
            self._print(filename+" "*pad+left+" "+final_right)
            if leave: sys.stdout.write("\n");sys.stdout.flush();self._last=0
            else: self._clear()
        except KeyboardInterrupt:
            self._clear();raise
    def demo(self):
        for f,s in [("file_name.py",23760),("assets.tar.gz",5_300_000),("config.yml",4096)]:
            self.download(f,size=s,leave=False)
        # leave a final visible line for the last file
        self.download("done.txt",size=1,leave=True)
