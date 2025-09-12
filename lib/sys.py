import subprocess
from lib.colors import RED, RESET
from lib.utils import sys_err, after_empty

def sys_command(sys_migration):
    if not sys_migration:
        after_empty("sys", "$ pck3r sys {update/upgrade/updgr}\nupdgr : update and full-upgrade, packages.")
        return
    action = sys_migration.lower()
    if action == "update":
        cmd = ["sudo", "apt", "update"]
    elif action == "upgrade":
        cmd = ["sudo", "apt", "upgrade"]
    elif action == "updgr":
        cmd = ["bash", "-c", "sudo apt update && sudo apt -y full-upgrade"]
    else:
        print(f"{sys_err('')}{RED}Invalid sys command: {action}{RESET}")
        return
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        pass
