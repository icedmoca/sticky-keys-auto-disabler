import psutil
import time
import json
import os
import winreg

GAMES_FILE = "games.txt"
BACKUP_FILE = "backup_registry.json"
STICKY_KEYS_PATH = r"Control Panel\Accessibility\StickyKeys"

def load_game_list():
    if not os.path.exists(GAMES_FILE):
        print(f"[!] {GAMES_FILE} not found. Create it with one game .exe per line.")
        return []
    with open(GAMES_FILE, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]

def is_game_running(game_list):
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() in game_list:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def get_sticky_keys_flag():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, STICKY_KEYS_PATH, 0, winreg.KEY_READ)
    val, _ = winreg.QueryValueEx(key, "Flags")
    winreg.CloseKey(key)
    return val

def set_sticky_keys_flag(value):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, STICKY_KEYS_PATH, 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "Flags", 0, winreg.REG_SZ, value)
    winreg.CloseKey(key)

def backup_original_setting():
    if os.path.exists(BACKUP_FILE):
        return
    original = get_sticky_keys_flag()
    with open(BACKUP_FILE, "w") as f:
        json.dump({"Flags": original}, f)
    print("[*] Backed up original Sticky Keys setting.")

def restore_original_setting():
    if not os.path.exists(BACKUP_FILE):
        return
    with open(BACKUP_FILE, "r") as f:
        data = json.load(f)
    set_sticky_keys_flag(data["Flags"])
    print("[-] Restored Sticky Keys setting.")

def main():
    print("[*] Sticky Keys Auto Disabler running.")
    games = load_game_list()
    if not games:
        return

    backup_original_setting()
    disabled = False

    try:
        while True:
            running = is_game_running(games)
            if running and not disabled:
                print("[+] Game detected — disabling Sticky Keys.")
                set_sticky_keys_flag("506")
                disabled = True
            elif not running and disabled:
                print("[-] Game closed — restoring Sticky Keys.")
                restore_original_setting()
                disabled = False
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        if disabled:
            restore_original_setting()

if __name__ == "__main__":
    main()
