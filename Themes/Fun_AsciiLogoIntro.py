import sys, time

class FunAsciiLogoIntro:
    def __init__(self):
        self.logo = ["  ___  "," / _ \\ ","| | | |","| |_| |"," \\___/ "]
    def demo(self, secs=3):
        for line in self.logo: print(line); time.sleep(secs/len(self.logo))
        print("Loading…"); time.sleep(0.4); print("Ready ✓")

# back-compat
AsciiLogoIntro = FunAsciiLogoIntro
