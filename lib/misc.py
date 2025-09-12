import subprocess
from os import chdir
from lib.utils import sys_ok, sys_err
from lib.colors import RED, RESET

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

def version_command():
    print(f"{sys_ok('')}version : 1.0")

def print_help():
    from lib.utils import print_help as ph
    ph()
