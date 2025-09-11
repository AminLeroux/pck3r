#!/usr/bin/env python3
import argparse
import subprocess
import sys
from os import chdir

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def sys_err(msg):
    return f"\n{RED}尸⼕长㇌尺 : ERROR !\n{RED}{msg}{RESET}"

def sys_ok(msg):
    return f"\n{GREEN}OK{GREEN}尸⼕长㇌尺 :\n {GREEN}{msg}{RESET}"

def print_help():
    # Try to read /bin/pck3r-help first
    help_path = "/bin/pck3r-help"
    try:
        with open(help_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        # fallback to local README.md starting from line 24
        readme_path = "README.md"
        try:
            with open(readme_path, 'r') as f:
                lines = f.readlines()
                if len(lines) > 24:
                    content = ''.join(lines[24:])
                else:
                    content = ''.join(lines)
        except FileNotFoundError:
            print(sys_err("Help file not found"))
            return
    print(f"{YELLOW}{content}{RESET}")

def after_empty(command, help_contents):
    help_text = help_contents if help_contents else f"$ pck3r {command} hello"
    print(f"{sys_err('')}{RED}After \"{command}\" is empty!\n{YELLOW}{help_text}{RESET}")

def pkg_find(package_name):
    if not package_name:
        after_empty("pkg", "$ pck3r pkg <package>")
        return
    search_term = f"{package_name}.+"
    try:
        subprocess.run(["apt", "search", search_term], check=True)
    except subprocess.CalledProcessError:
        pass

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

def clear_command():
    try:
        subprocess.run(["clear"], check=True)
        print(sys_ok("This is a funny clear command :D"))
    except subprocess.CalledProcessError:
        pass

def update_command():
    try:
        chdir('/tmp')
        subprocess.run([
            "bash", "-c",
            "sudo rm -rf pck3r && sudo git clone https://github.com/amzy31/pck3r pck3r && cd pck3r && sudo make install"
        ], check=True)
        print(sys_ok("pck3r updated successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}Failed to update pck3r.{RESET}")

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
    script = r"""
echo "Installing Node.js..."
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - ;
sudo apt install -y nodejs ;
sudo apt-get update ;
"""
    try:
        subprocess.run(["bash", "-c", script], check=True)
        print(sys_ok("Node.js installed successfully!"))
    except subprocess.CalledProcessError:
        print(f"{sys_err('')}{RED}\nPlease retry...\n$pck3r install nodejs{RESET}")

def install_ohmyzsh():
    print("Installing Oh My Zsh...")
    try:
        # Install git and zsh
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
            r"sh -c \"$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\""
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

def version_command():
    print(f"{sys_ok('')}version : 1.0")

def main():
    parser = argparse.ArgumentParser(
        prog="pck3r",
        description="A versatile program for Ubuntu/Debian package management",
        add_help=False
    )

    parser.add_argument("--help", "-h", action="store_true", help="Show help")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Clear command
    subparsers.add_parser("clear", help="Clear terminal screen")

    # Update command
    subparsers.add_parser("update", help="Update pck3r")

    # Install command
    install_parser = subparsers.add_parser("install", help="Install packages")
    install_parser.add_argument("package", nargs="?", help="Package to install")

    # Sys command
    sys_parser = subparsers.add_parser("sys", help="System commands")
    sys_parser.add_argument("action", nargs="?", help="System action (update/upgrade/updgr)")

    # Pkg command
    pkg_parser = subparsers.add_parser("pkg", help="Search packages")
    pkg_parser.add_argument("package", nargs="?", help="Package to search")

    # Version command
    subparsers.add_parser("version", help="Show version")

    args = parser.parse_args()

    if args.help or not args.command:
        print_help()
        return

    if args.command == "clear":
        clear_command()
    elif args.command == "update":
        update_command()
    elif args.command == "install":
        install_command(args.package)
    elif args.command == "sys":
        sys_command(args.action)
    elif args.command == "pkg":
        pkg_find(args.package)
    elif args.command == "version":
        version_command()
    else:
        print(f"{sys_err('')}{RED}No command provided. Use \"--help\" for a list of available commands.{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
