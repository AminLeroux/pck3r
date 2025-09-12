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
        print("Installing Oh My Zsh...")
        subprocess.run([
            "bash", "-c",
            "curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | bash"
        ], check=True)
        print(sys_ok("Oh My Zsh installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Oh My Zsh installation failed.{RESET}")

def install_google_chrome():
    try:
        print("Installing Google Chrome...")
        subprocess.run([
            "bash", "-c",
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/google-chrome.deb && sudo apt install -y /tmp/google-chrome.deb"
        ], check=True)
        print(sys_ok("Google Chrome installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Google Chrome installation failed.{RESET}")

def install_steam():
    try:
        print("Installing Steam...")
        subprocess.run([
            "bash", "-c",
            "wget https://steamcdn-a.akamaihd.net/client/installer/steam.deb -O /tmp/steam.deb && sudo apt install -y /tmp/steam.deb"
        ], check=True)
        print(sys_ok("Steam installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Steam installation failed.{RESET}")

def install_discord():
    try:
        print("Installing Discord...")
        subprocess.run([
            "bash", "-c",
            "wget https://discordapp.com/api/download?platform=linux&format=deb -O /tmp/discord.deb && sudo apt install -y /tmp/discord.deb"
        ], check=True)
        print(sys_ok("Discord installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Discord installation failed.{RESET}")

def install_vscode():
    try:
        print("Installing Visual Studio Code...")
        subprocess.run([
            "bash", "-c",
            "wget https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64 -O /tmp/vscode.deb && sudo apt install -y /tmp/vscode.deb"
        ], check=True)
        print(sys_ok("Visual Studio Code installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Visual Studio Code installation failed.{RESET}")

def install_skype():
    try:
        print("Installing Skype...")
        subprocess.run([
            "bash", "-c",
            "wget https://go.skype.com/skypeforlinux-64.deb -O /tmp/skype.deb && sudo apt install -y /tmp/skype.deb"
        ], check=True)
        print(sys_ok("Skype installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Skype installation failed.{RESET}")

def install_zoom():
    try:
        print("Installing Zoom...")
        subprocess.run([
            "bash", "-c",
            "wget https://zoom.us/client/latest/zoom_amd64.deb -O /tmp/zoom.deb && sudo apt install -y /tmp/zoom.deb"
        ], check=True)
        print(sys_ok("Zoom installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Zoom installation failed.{RESET}")

def install_vlc():
    try:
        print("Installing VLC...")
        subprocess.run([
            "bash", "-c",
            "sudo add-apt-repository ppa:videolan/stable-daily -y && sudo apt update && sudo apt install -y vlc"
        ], check=True)
        print(sys_ok("VLC installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}VLC installation failed.{RESET}")

def install_virtualbox():
    try:
        print("Installing VirtualBox...")
        subprocess.run([
            "bash", "-c",
            "wget https://download.virtualbox.org/virtualbox/debian/pool/main/o/virtualbox/virtualbox-7.0_7.0.18-162988~Ubuntu~noble_amd64.deb -O /tmp/virtualbox.deb && sudo apt install -y /tmp/virtualbox.deb"
        ], check=True)
        print(sys_ok("VirtualBox installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}VirtualBox installation failed.{RESET}")

def install_wine():
    try:
        print("Installing Wine...")
        subprocess.run([
            "bash", "-c",
            "wget https://dl.winehq.org/wine-builds/ubuntu/dists/noble/winehq.key -O /tmp/winehq.key && sudo apt-key add /tmp/winehq.key && sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ noble main' && sudo apt update && sudo apt install -y --install-recommends winehq-stable"
        ], check=True)
        print(sys_ok("Wine installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Wine installation failed.{RESET}")

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

    # Dictionary for built-in install functions
    builtin_installs = {
        "nodejs": install_nodejs,
        "ohmyzsh": install_ohmyzsh,
        "firefox": install_firefox,
        "google-chrome": install_google_chrome,
        "steam": install_steam,
        "discord": install_discord,
        "vscode": install_vscode,
        "skype": install_skype,
        "zoom": install_zoom,
        "vlc": install_vlc,
        "virtualbox": install_virtualbox,
        "wine": install_wine,
    }

    if package in builtin_installs:
        builtin_installs[package]()
    else:
        handle_generic_install(package)
