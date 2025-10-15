#!/usr/bin/env python3
import sys
from Themes import (
    InstallerStyle1,InstallerStyle2,InstallerStyle3,InstallerStyle4,InstallerStyle5,
    LoaderThrobber,LoaderBounce,LoaderWave,LoaderRing,
    NetHandshake,NetReconnect,NetThroughput,NetHealthGrid,NetRouteProbe,NetTokenLifespan,NetProxyNegotiation,
    IOSegmented,IOExtractor,IOIndexer,IOChecksumParade,IOCacheMeter,IOSparseCopyViz,
    MonLogTail,MonHeartbeat,MonCheckMatrix,MonServiceTimeline,MonAlertWaterfall,MonPerfBudget,
    UXWizard,UXTicker,UXEmojiLite,UXThemeSkins,UXWidthAwareTrunc,UXColorblindSafe,UXSoundHooks,UXPersistResume,
    DevVerboseToggleLive,DevLatencyHistogram,DevTraceMarkers,
    FunAsciiLogoIntro,FunAchievementBadges,
    VisFunnel,VisStackedBars,VisThermometer,VisRadarSweep,VisCountdownGate,
    FlowFormWizardInline,FlowChoiceCarousel,FlowQuickActionsPalette,FlowYesNoTimeout,FlowDryRunDiff,
    RelAutoRetryLadder,RelQuarantineQueue,RelRollbackTracker,
    SecPolicyGateChecks,SecSecretsExposureMeter,SecSbomScanStrip
)
def clear():print("\x1b[2J\x1b[H",end="")
def pause():input("\nPress Enter to continue...")
# ===================== Install styles =====================
def demo_InstallerStyle1():clear();InstallerStyle1(["websocket","redis-cache","backend","redis-queue","frontend","cron","proxy","db","scheduler","queue-short","configurator","queue-long"],parallel=4,total=45).run();pause()
def demo_InstallerStyle2():clear();InstallerStyle2().demo();pause()
def demo_InstallerStyle3():clear();InstallerStyle3().demo();pause()
def demo_InstallerStyle4():clear();InstallerStyle4().demo();pause()
def demo_InstallerStyle5():clear();InstallerStyle5(80).demo();pause()

# ===================== Loading / Compute =====================
def demo_LoaderThrobber():clear();LoaderThrobber().demo();pause()
def demo_LoaderBounce():clear();LoaderBounce().demo();pause()
def demo_LoaderWave():clear();LoaderWave().demo();pause()
def demo_LoaderRing():clear();LoaderRing().demo();pause()

# ===================== Network / Connect =====================
def demo_NetHandshake():clear();NetHandshake().demo();pause()
def demo_NetReconnect():clear();NetReconnect().demo();pause()
def demo_NetThroughput():clear();NetThroughput().demo();pause()
def demo_NetHealthGrid():clear();NetHealthGrid().demo();pause()
def demo_NetRouteProbe():clear();NetRouteProbe().demo();pause()
def demo_NetTokenLifespan():clear();NetTokenLifespan().demo();pause()
def demo_NetProxyNegotiation():clear();NetProxyNegotiation().demo();pause()

# ===================== Data / IO =====================
def demo_IOSegmented():clear();IOSegmented().demo();pause()
def demo_IOExtractor():clear();IOExtractor().demo();pause()
def demo_IOIndexer():clear();IOIndexer().demo();pause()
def demo_IOChecksumParade():clear();IOChecksumParade().demo();pause()
def demo_IOCacheMeter():clear();IOCacheMeter().demo();pause()
def demo_IOSparseCopyViz():clear();IOSparseCopyViz().demo();pause()

# ===================== Monitoring / Diagnostics =====================
def demo_MonLogTail():clear();MonLogTail().demo();pause()
def demo_MonHeartbeat():clear();MonHeartbeat().demo();pause()
def demo_MonCheckMatrix():clear();MonCheckMatrix().demo();pause()
def demo_MonServiceTimeline():clear();MonServiceTimeline().demo();pause()
def demo_MonAlertWaterfall():clear();MonAlertWaterfall().demo();pause()
def demo_MonPerfBudget():clear();MonPerfBudget().demo();pause()

# ===================== Reliability / Resilience =====================
def demo_RelAutoRetryLadder():clear();RelAutoRetryLadder().demo();pause()
def demo_RelQuarantineQueue():clear();RelQuarantineQueue().demo();pause()
def demo_RelRollbackTracker():clear();RelRollbackTracker().demo();pause()

# ===================== Security / Compliance =====================
def demo_SecPolicyGateChecks():clear();SecPolicyGateChecks().demo();pause()
def demo_SecSecretsExposureMeter():clear();SecSecretsExposureMeter().demo();pause()
def demo_SecSbomScanStrip():clear();SecSbomScanStrip().demo();pause()

# ===================== UX / Polish =====================
def demo_UXWizard():clear();UXWizard().demo();pause()
def demo_UXTicker():clear();UXTicker().demo();pause()
def demo_UXEmojiLite():clear();UXEmojiLite().demo();pause()
def demo_UXThemeSkins():clear();UXThemeSkins().demo();pause()
def demo_UXWidthAwareTrunc():clear();UXWidthAwareTrunc().demo();pause()
def demo_UXColorblindSafe():clear();UXColorblindSafe().demo();pause()
def demo_UXSoundHooks():clear();UXSoundHooks().demo();pause()
def demo_UXPersistResume():clear();UXPersistResume().demo();pause()

# ===================== Visual / Progress =====================
def demo_VisFunnel():clear();VisFunnel().demo();pause()
def demo_VisStackedBars():clear();VisStackedBars().demo();pause()
def demo_VisThermometer():clear();VisThermometer().demo();pause()
def demo_VisRadarSweep():clear();VisRadarSweep().demo();pause()
def demo_VisCountdownGate():clear();VisCountdownGate().demo();pause()

# ===================== Flow =====================
def demo_FlowFormWizardInline():clear();FlowFormWizardInline().demo();pause()
def demo_FlowChoiceCarousel():clear();FlowChoiceCarousel().demo();pause()
def demo_FlowQuickActionsPalette():clear();FlowQuickActionsPalette().demo();pause()
def demo_FlowYesNoTimeout():clear();FlowYesNoTimeout().demo();pause()
def demo_FlowDryRunDiff():clear();FlowDryRunDiff().demo();pause()

# ===================== Developer / Debug =====================
def demo_DevVerboseToggleLive():clear();DevVerboseToggleLive().demo();pause()
def demo_DevLatencyHistogram():clear();DevLatencyHistogram().demo();pause()
def demo_DevTraceMarkers():clear();DevTraceMarkers().demo();pause()

# ===================== Fun / Branding =====================
def demo_FunAsciiLogoIntro():clear();FunAsciiLogoIntro().demo();pause()
def demo_FunAchievementBadges():clear();FunAchievementBadges().demo();pause()

def menu_Install_styles():
 while True:
  clear();print("===== Install styles =====\n1) Style 1\n2) Style 2\n3) Style 3 (Checklist)\n4) Style 4 (Spinner per step)\n5) Style 5 (Dot leaders)\nB) Back to Main\nE) Exit");c=input("> ").strip().lower()
  if c=="1":demo_InstallerStyle1()
  elif c=="2":demo_InstallerStyle2()
  elif c=="3":demo_InstallerStyle3()
  elif c=="4":demo_InstallerStyle4()
  elif c=="5":demo_InstallerStyle5()
  elif c=="b":return
  elif c=="e":sys.exit(0)

def menu_Loading_Compute_styles():
 while True:
  clear();print("===== Loading/Compute styles =====\n1) Throbber + Status Line\n2) Bouncing Bar\n3) Wave/Sine Loader\n4) Progress Ring (ASCII)\nB) Back to Main\nE) Exit");c=input("> ").strip().lower()
  if c=="1":demo_LoaderThrobber()
  elif c=="2":demo_LoaderBounce()
  elif c=="3":demo_LoaderWave()
  elif c=="4":demo_LoaderRing()
  elif c=="b":return
  elif c=="e":sys.exit(0)

def menu_Network_Connect_styles():
 while True:
  clear();print("===== Network/Connect styles =====\n1) Handshake Timeline\n2) Reconnect w/ Backoff\n3) Throughput Gauge\n4) Session Health Grid\n5) Route Probe\n6) Token Lifespan Meter\n7) Proxy Negotiation Strip\nB) Back to Main\nE) Exit");c=input("> ").strip().lower()
  if c=="1":demo_NetHandshake()
  elif c=="2":demo_NetReconnect()
  elif c=="3":demo_NetThroughput()
  elif c=="4":demo_NetHealthGrid()
  elif c=="5":demo_NetRouteProbe()
  elif c=="6":demo_NetTokenLifespan()
  elif c=="7":demo_NetProxyNegotiation()
  elif c=="b":return
  elif c=="e":sys.exit(0)

def menu_Data_IO_styles():
 while True:
  clear();print("===== Data/IO styles =====\n1) Segmented Download\n2) Extractor\n3) Indexer\n4) Checksum Parade\n5) Cold/Warm Cache Meter\n6) Sparse Copy Visualizer\nB) Back to Main\nE) Exit");c=input("> ").strip().lower()
  if c=="1":demo_IOSegmented()
  elif c=="2":demo_IOExtractor()
  elif c=="3":demo_IOIndexer()
  elif c=="4":demo_IOChecksumParade()
  elif c=="5":demo_IOCacheMeter()
  elif c=="6":demo_IOSparseCopyViz()
  elif c=="b":return
  elif c=="e":sys.exit(0)

def menu_Monitoring_Diagnostics():
 while True:
  clear();print("===== Monitoring/Diagnostics =====\n1) Live Log Tail + Status Header\n2) Heartbeat/Healthbeat\n3) Check Matrix\n4) Service Timeline\n5) Alert Waterfall\n6) Perf Budget\nB) Back to Main\nE) Exit");c=input("> ").strip().lower()
  if c=="1":demo_MonLogTail()
  elif c=="2":demo_MonHeartbeat()
  elif c=="3":demo_MonCheckMatrix()
  elif c=="4":demo_MonServiceTimeline()
  elif c=="5":demo_MonAlertWaterfall()
  elif c=="6":demo_MonPerfBudget()
  elif c=="b":return
  elif c=="e":sys.exit(0)

def menu_Reliability_Resilience():
 while True:
  clear();print("===== Reliability/Resilience =====\n1) Auto-Retry Ladder\n2) Quarantine Queue\n3) Rollback Tracker\nB) Back to Main\nE) Exit");c=input("> ").strip().lower()
  if c=="1":demo_RelAutoRetryLadder()
  elif c=="2":demo_RelQuarantineQueue()
  elif c=="3":demo_RelRollbackTracker()
  elif c=="b":return
  elif c=="e":sys.exit(0)

def menu_Security_Compliance():
 while True:
  clear();print("===== Security/Compliance =====\n1) Policy Gate Checks\n2) Secrets Exposure Meter\n3) SBOM Scan Strip\nB) Back to Main\nE) Exit");c=input("> ").strip().lower()
  if c=="1":demo_SecPolicyGateChecks()
  elif c=="2":demo_SecSecretsExposureMeter()
  elif c=="3":demo_SecSbomScanStrip()
  elif c=="b":return
  elif c=="e":sys.exit(0)

def menu_UX_Polish_patterns():
 while True:
  clear();print("===== UX/Polish patterns =====\n1) Prompt-Driven Wizard\n2) Compact Ticker\n3) Emoji-Lite Theme\n4) Theme Skins\n5) Width-aware Truncation\n6) Colorblind-safe Palette\n7) Sound/Beep Hooks\n8) Persist & Resume\nB) Back to Main\nE) Exit");c=input("> ").strip().lower()
  if c=="1":demo_UXWizard()
  elif c=="2":demo_UXTicker()
  elif c=="3":demo_UXEmojiLite()
  elif c=="4":demo_UXThemeSkins()
  elif c=="5":demo_UXWidthAwareTrunc()
  elif c=="6":demo_UXColorblindSafe()
  elif c=="7":demo_UXSoundHooks()
  elif c=="8":demo_UXPersistResume()
  elif c=="b":return
  elif c=="e":sys.exit(0)

def menu_Developer_Debug():
 while True:
  clear();print("===== Developer/Debug =====\n1) Verbose Toggle Live\n2) Latency Histogram\n3) Trace Markers\nB) Back to Main\nE) Exit");c=input("> ").strip().lower()
  if c=="1":demo_DevVerboseToggleLive()
  elif c=="2":demo_DevLatencyHistogram()
  elif c=="3":demo_DevTraceMarkers()
  elif c=="b":return
  elif c=="e":sys.exit(0)

def menu_Fun_Branding():
 while True:
  clear();print("===== Fun/Branding =====\n1) Tiny ASCII Logo Intro\n2) Achievement Badges\nB) Back to Main\nE) Exit");c=input("> ").strip().lower()
  if c=="1":demo_FunAsciiLogoIntro()
  elif c=="2":demo_FunAchievementBadges()
  elif c=="b":return
  elif c=="e":sys.exit(0)

def main():
 while True:
  clear();print("===== Welcome to =====\n===== CLI Themes =====\n1) Install styles.\n2) Loading/Compute styles.\n3) Network/Connect styles.\n4) Data/IO styles.\n5) Monitoring/Diagnostics.\n6) Reliability/Resilience.\n7) Security/Compliance.\n8) UX/Polish patterns.\n9) Developer/Debug.\n10) Fun/Branding.\nE) Exit");c=input("> ").strip().lower()
  if c=="1":menu_Install_styles()
  elif c=="2":menu_Loading_Compute_styles()
  elif c=="3":menu_Network_Connect_styles()
  elif c=="4":menu_Data_IO_styles()
  elif c=="5":menu_Monitoring_Diagnostics()
  elif c=="6":menu_Reliability_Resilience()
  elif c=="7":menu_Security_Compliance()
  elif c=="8":menu_UX_Polish_patterns()
  elif c=="9":menu_Developer_Debug()
  elif c=="10":menu_Fun_Branding()
  elif c=="e":break

if __name__=="__main__":
 try: main()
 except KeyboardInterrupt: print()
