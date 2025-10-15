
# CLI Themes

A showroom of **terminal UI patterns** for installers, loaders, network flows, monitoring, and more—ready to copy into your own apps. Launch the menu and preview any style with an interactive demo.

> Works on Linux/macOS/Windows terminals that support ANSI escape codes.

---

## ✨ Features

* **Installers**: multi-step, spinners-per-step, dot leaders, etc.
* **Loading/Compute**: throbbers, bouncing bars, waves, ASCII rings.
* **Network/Connect**: handshake timeline, backoff-retry, throughput gauge, health grid.
* **Data/IO**: segmented downloads, extractors, indexers, checksum parade.
* **Monitoring**: live log tail, heartbeat, check matrix, service timeline, perf budget.
* **Reliability**: auto-retry ladder, quarantine queue, rollback tracker.
* **Security**: policy gates, secrets exposure meter, SBOM scan strip.
* **UX/Polish**: wizard prompts, compact ticker, emoji-lite, skins, width-aware truncation, sound hooks, persist & resume.
* **Visual/Progress**: funnel, stacked bars, thermometer, radar sweep, countdown gate.
* **Flow**: choice carousel, quick actions palette, yes/no with timeout, dry-run diff.
* **Developer/Debug**: verbose toggle (live), latency histogram, trace markers.
* **Fun/Branding**: tiny ASCII logo intro, achievement badges.

---

## 🗂 Project structure

```
CLI themes/
├─ ShowRoom.py
└─ Themes/
   ├─ __init__.py
   ├─ Installer_Style_1.py … Installer_Style_5.py
   ├─ Loading_Bounce.py, Loading_Ring.py, Loading_Throbber.py, Loading_Wave.py
   ├─ Net_*.py          (Handshake, Reconnect, Throughput, HealthGrid, RouteProbe, TokenLifespan, ProxyNegotiation)
   ├─ IO_*.py           (Segmented, Extractor, Indexer, ChecksumParade, CacheMeter, SparseCopyViz)
   ├─ Mon_*.py          (LogTail, Heartbeat, CheckMatrix, ServiceTimeline, AlertWaterfall, PerfBudget)
   ├─ Rel_*.py          (AutoRetryLadder, QuarantineQueue, RollbackTracker)
   ├─ Sec_*.py          (PolicyGateChecks, SecretsExposureMeter, SbomScanStrip)
   ├─ UX_*.py           (Wizard, Ticker, EmojiLite, ThemeSkins, WidthAwareTrunc, ColorblindSafe, SoundHooks, PersistResume)
   ├─ Vis_*.py          (Funnel, StackedBars, Thermometer, RadarSweep, CountdownGate)
   └─ Flow_*.py         (FormWizardInline, ChoiceCarousel, QuickActionsPalette, YesNoTimeout, DryRunDiff)
```

Each file exports a class (e.g., `NetRouteProbe`) with a simple `demo()` you can run from the showroom.

---

## 🚀 Quick start

**Requirements**: Python 3.8+ (ANSI-capable terminal recommended)

```bash
# From inside "CLI themes/"
python3 ShowRoom.py
```

Use the arrow keys / number keys:

* Main menu → choose a category
* Pick an item to see the animated demo
* `B` returns to main, `E` exits, `Ctrl+C` always safe

---

## 📦 Install (optional venv)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python3 ShowRoom.py
```

No external packages required; everything uses Python stdlib (`time`, `random`, `sys`, `shutil`, etc.).

---

## 🧩 Using a theme in your app

Every theme class has a minimal interface:

```python
from Themes import NetRouteProbe  # import via __init__.py re-exports

probe = NetRouteProbe()
probe.demo(secs=3)  # run as a standalone UI snippet

# Or copy/paste the class (or selected methods) into your codebase and integrate
# with your real task loops (downloads, network calls, builds, etc.).
```

Most demos do line-in-place updates using `\r` + ANSI clear-line `\x1b[2K`; they’re easy to adapt into your own loops. For example, progress callbacks can call the class’s `_p("status…")` method to rewrite a single status line.

---

## 🛠 Adding a new theme

1. Create `Themes/My_AwesomeThing.py` with a class name matching the prefix rules
   (e.g., `class UXAwesomeThing:` or `class NetAwesomeThing:`).
2. Export it in `Themes/__init__.py`:

```python
from .My_AwesomeThing import UXAwesomeThing
__all__.append("UXAwesomeThing")
```

3. Add a one-liner demo launcher in `ShowRoom.py`:

```python
def demo_UXAwesomeThing(): clear(); UXAwesomeThing().demo(); pause()
```

4. Wire it into the right submenu.

> Tip: Many modules include a *back-compat alias* (e.g., `AwesomeThing = UXAwesomeThing`) so older names still work.

---

## 🧪 Demo functions (pattern)

Showroom entries use consistent one-liners:

```python
def demo_NetRouteProbe(): clear(); NetRouteProbe().demo(); pause()
def demo_UXWidthAwareTrunc(): clear(); UXWidthAwareTrunc().demo(); pause()
```

This keeps the menu logic simple and predictable.

---

## 🔧 Troubleshooting

* **NameError: `demo_X` not defined**
  You added a menu option but not the `demo_*` function. Add it near other demos.

* **ImportError for a theme class**
  Ensure `Themes/__init__.py` exports the class *and* the class name matches the file prefix (`UX_`, `Net_`, `Mon_`, etc.). Example: `UX_ThemeSkins.py` must define `class UXThemeSkins`.

* **Windows “weird characters”**
  Enable ANSI in your terminal (Windows 10+ supports it in recent consoles).
  If using old `cmd.exe`, try Windows Terminal or PowerShell.

* **Terminal too narrow**
  Some demos compute width via `shutil.get_terminal_size((80,20)).columns`. Resize the window or adjust the code’s default.

---

## 🧭 Batch scaffolding (optional)

There’s a helper script `batch_add_themes.py` that:

* Generates stubs for all ideas
* Rebuilds `Themes/__init__.py` exports
* Rewrites `ShowRoom.py` menus

Run it from the project folder:

```bash
python3 batch_add_themes.py
python3 ShowRoom.py
```

---

## 🗺 Roadmap (ideas to polish)

* Colorized variants (auto-fallback to ASCII)
* Keyboard interactivity (left/right in ChoiceCarousel, `v` to toggle verbose, etc.)
* Real metrics adapters (attach to actual downloads, pings, logs)
* Unit tests for width/truncation and progress formatting

---

## 📄 License

Use freely in your projects. Attribution appreciated but not required.

---

## 🙌 Credits

Built with ❤️ to make terminal installers & CLIs look **pro** in a few lines.

---