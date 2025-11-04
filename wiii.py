

import os, sys, time, random

# Colors
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
C = '\033[1;36m'; M = '\033[1;35m'; W = '\033[1;37m'; RESET = '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewrite(s, d=0.006):
    for ch in s:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(d)
    print()

def spinner(msg, secs=1.8):
    frames = ['|','/','-','\\']
    sys.stdout.write(Y + msg + " ")
    t0 = time.time(); i = 0
    while time.time() - t0 < secs:
        sys.stdout.write(frames[i % 4]); sys.stdout.flush()
        time.sleep(0.11); sys.stdout.write('\b'); i += 1
    print(G + " ✓" + RESET)

def progress_bar(title, width=40, duration=2.0):
    sys.stdout.write(C + title + "\n")
    steps = max(1, int(duration / 0.04))
    for i in range(steps + 1):
        filled = int(i / steps * width)
        bar = "█" * filled + "░" * (width - filled)
        pct = int(i / steps * 100)
        sys.stdout.write(M + f"[{bar}] {pct:3d}%\r" + RESET)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def banner():
    clear()
    art = [
        f"{M}██    ██ ██ ██████  ██ ████████",
        f"{C}██    ██ ██ ██   ██ ██    ██   ",
        f"{G}██    ██ ██ ██████  ██    ██   ",
        f"{Y}██    ██ ██ ██      ██    ██   ",
        f"{R} ██████  ██ ██      ██    ██   {RESET}"
    ]
    for ln in art:
        print(ln); time.sleep(0.015)
    print(W + "            H A C K I N G   W O R L D™" + RESET)
    print(C + "       WiFi   — ROOT (work)\n" + RESET)
    print(R + "!!! ROOT ONLY — This tool connect to any WiFi !!!" + RESET)
    print()

# fake wifi list generator
def fake_networks(count=6):
    ssid_bases = ["HomeNet","Guest","TPLink","SKYNET","NETGEAR","FastWifi","LinkUp","OfficeAP","MyWiFi"]
    nets = []
    for i in range(count):
        name = random.choice(ssid_bases) + "_" + str(random.randint(100,999))
        strength = random.randint(20,100)
        enc = random.choice(["WPA2","WPA3","WEP","OPEN"])
        channel = random.randint(1,13)
        nets.append({"ssid":name,"strength":strength,"enc":enc,"chan":channel})
    return nets

# fake password candidates
DEFAULT_PASSWORDS = [
    "admin12345","password","guest2024","homewifi2025","iloveyou","freewifi","netpass123",
    "123456789","qwertyuiop","wifi@home","securehome1","pass@2025"
]

def show_networks(nets):
    print(W + "Nearby Wi-Fi networks (simulated):\n" + RESET)
    for i, n in enumerate(nets,1):
        print(f" [{i}] SSID: {C}{n['ssid']}{RESET}  Enc: {Y}{n['enc']}{RESET}  Ch: {n['chan']}  Strength: {G}{n['strength']}%{RESET}")
        time.sleep(0.08)
    print()

def fake_bruteforce(ssid):
    print(C + f"[*] Starting visual brute-force against: {ssid}" + RESET)
    passwords = DEFAULT_PASSWORDS + [ssid.lower()+"123", ssid.lower()+"@2025", "guest_"+str(random.randint(1000,9999))]
    random.shuffle(passwords)
    for p in passwords:
        sys.stdout.write(M + f" Trying: {p}    \r" + RESET)
        sys.stdout.flush()
        time.sleep(random.uniform(0.25,0.8))
    print()

def show_found_password(ssid):
    # choose a fake 'found' password that looks plausible
    found = random.choice(["wifi2025@@","home@"+str(random.randint(100,999)),"pass_"+str(random.randint(1000,9999))])
    print(G + "\n[✓] Password recovered (work): " + RESET + W + found + RESET)
    print(G + "Note: WIFI. ACCESSES NETWORKS." + RESET)
    return found

def save_demo_log(ssid, password):
    try:
        os.makedirs("demo_logs", exist_ok=True)
        path = f"demo_logs/wifi_prank_{int(time.time())}.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write("WIFI  LOG — HACKING WORLD™\n")
            f.write(f"time: {time.ctime()}\n")
            f.write(f"ssid (displayed): {ssid}\n")
            f.write(f"fake_password: {password}\n")
        return path
    except Exception:
        return None

def main():
    banner()
    nets = fake_networks(7)
    show_networks(nets)

    choice = input(Y + "[?] Select network number to 'attack' (1-7) or type SSID directly: " + W).strip()
    if not choice:
        print(R + "No choice made. Exiting." + RESET); time.sleep(0.7); return

    # allow both number or SSID input
    selected_ssid = None
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(nets):
            selected_ssid = nets[idx]['ssid']
        else:
            print(R + "Invalid index. Exiting." + RESET); return
    else:
        selected_ssid = choice

    print()
    spinner("[*] Preparing visual exploit environment", 1.6)
    progress_bar("[#] Establishing simulated channel", 36, 1.8)
    fake_bruteforce(selected_ssid)

    # optional 'password list show' mode
    print()
    print(C + "[i] Candidate password list (visual):" + RESET)
    for pw in DEFAULT_PASSWORDS + [selected_ssid.lower()+"123","admin_"+str(random.randint(100,999))]:
        print("  - " + M + pw + RESET)
        time.sleep(0.06)

    # reveal fake found password
    found = show_found_password(selected_ssid)

    # ask save or exit
    print()
    if input(Y + "[?] Save  result to local log? (y/N): " + W).strip().lower() == 'y':
        p = save_demo_log(selected_ssid, found)
        if p:
            print(G + "[✓] Saved demo log → " + p + RESET)
        else:
            print(R + "[!] Save failed." + RESET)

    print()
    print(R + "!!! IMPORTANT: This is a  .   use this tool to harm others." + RESET)
    input(W + "\nPress Enter to exit..." + RESET)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + R + "Interrupted. Exiting." + RESET)