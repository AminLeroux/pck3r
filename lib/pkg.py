import subprocess
from lib.utils import after_empty, sys_ok
from lib.colors import GREEN, RESET

def pkg_find(package_name):
    builtin_packages = [
        "nodejs", "ohmyzsh", "firefox", "google-chrome", "steam",
        "discord", "vscode", "skype", "zoom", "vlc", "virtualbox", "wine"
    ]
    if not package_name:
        # List built-in pck3r packages
        print(f"{GREEN}Built-in Pck3r packages:{RESET}")
        for pkg in builtin_packages:
            print(f"  - {pkg}")
        return
    package_name_lower = package_name.strip().lower()
    if package_name_lower in builtin_packages:
        print(sys_ok(f"built-in package detected : {package_name_lower}"))
        return
    # Search for apt packages
    search_term = f"{package_name}.+"
    try:
        subprocess.run(["apt", "search", search_term], check=True)
    except subprocess.CalledProcessError:
        pass
