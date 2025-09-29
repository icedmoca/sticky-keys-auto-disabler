# Sticky Keys Auto Disabler

Automatically disables Sticky Keys when your selected games are running — and restores them afterward.  
Built for accessibility, focus, and uninterrupted gameplay.

---

## Features

- ✅ Auto-detects running games from a list
- ✅ Disables Sticky Keys in the Windows registry
- ✅ Restores your original settings when game exits
- ✅ Lightweight, runs silently in background
- ♿ Accessibility-first: perfect for disabled users or heavy Shift users

---

## Requirements

- Windows 10 or 11
- Python 3.x
- Admin privileges (to modify registry)

---

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/icedmoca/sticky-keys-auto-disabler.git
   cd sticky-keys-auto-disabler
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Edit your games list**  
   Open `games.txt` and add the `.exe` names of your games (one per line). Example:
   ```
   eldenring.exe
   halo.exe
   valorant.exe
   ```

4. **Run the script**
   ```bash
   python sticky_disabler.py
   ```

---

## 🧠 How it Works

- Monitors running processes using [`psutil`](https://pypi.org/project/psutil/)
- Disables Sticky Keys by updating this registry key:

  ```
  HKEY_CURRENT_USER\Control Panel\Accessibility\StickyKeys\Flags
  ```

- Automatically restores original registry setting after game closes

---

> **Warning:** This script modifies your Windows registry. Use responsibly.


- This script modifies your Windows registry — use responsibly
- Always exit the program cleanly to restore your original Sticky Keys setting
- Run with admin privileges to ensure it can write to the registry

---

## TODO / Contributions Welcome

- [ ] System tray app version
- [ ] Auto-start with Windows option
- [ ] GUI for editing game list
- [ ] One-click EXE build

---

## 📄 License

MIT License — free to use, modify, and share.

---

## 💬 Feedback

Got a feature idea? Open an issue or submit a PR.
