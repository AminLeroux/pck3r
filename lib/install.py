import os
import subprocess
from lib.colors import RED, GREEN, YELLOW, RESET
from lib.utils import sys_err, sys_ok, after_empty

def install_firefox():
    script = """
sudo install -d -m 0755 /etc/apt/keyrings
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000
' | sudo tee /etc/apt/preferences.d/mozilla
sudo apt-get update && sudo apt-get install firefox
"""
    try:
        subprocess.run(["bash", "-c", script], check=True)
        print(sys_ok("Firefox installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Firefox installation failed.{RESET}")

def install_nodejs():
    script = r'''
echo "Installing Node.js..."
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - ;
sudo apt install -y nodejs ;
sudo apt-get update ;'''
    try:
        subprocess.run(["bash", "-c", script], check=True)
        print(sys_ok("Node.js installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}\nPlease retry...\n$pck3r install nodejs{RESET}")

def install_ohmyzsh():
    try:
        # Install git and zsh
        print("Installing Oh My Zsh...")
        subprocess.run(["sudo", "apt", "install", "-y", "git", "zsh"], check=True)

        # Check if curl is available
        try:
            subprocess.run(["curl", "--version"], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            print(f"{sys_err('')}{RED}\"curl\" is required for using \"oh-my-zsh\" ; installing curl...{RESET}")
            subprocess.run(["sudo", "apt", "install", "-y", "curl"], check=True)

        # Install Oh My Zsh
        subprocess.run([
            "bash", "-c",
            "curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | bash"
        ], check=True)
        print(sys_ok("Oh My Zsh installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Oh My Zsh installation failed.{RESET}")

def handle_generic_install(package_name):
    print(f"{sys_ok('')}{YELLOW}[WAIT FOR PROCESSING]{RESET}")
    try:
        subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Package(s) or Command(s) not found: {package_name}{RESET}")

def install_command(package_name):
    if not package_name:
        after_empty("install", "$ pck3r install {package name}")
        return
    package = package_name.strip().lower()
    if package == "nodejs":
        install_nodejs()
    elif package == "ohmyzsh":
        install_ohmyzsh()
    elif package == "firefox":
        install_firefox()
    else:
        handle_generic_install(package)
