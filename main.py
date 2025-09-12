#!/usr/bin/env python3
import argparse
import sys

from lib.colors import RED, RESET
from lib.utils import print_help, sys_err
from lib.misc import clear_command, update_command, version_command
from lib.install import install_command
from lib.sys import sys_command
from lib.pkg import pkg_find

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
