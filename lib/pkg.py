import subprocess
from lib.utils import after_empty

def pkg_find(package_name):
    if not package_name:
        after_empty("pkg", "$ pck3r pkg <package>")
        return
    search_term = f"{package_name}.+"
    try:
        subprocess.run(["apt", "search", search_term], check=True)
    except subprocess.CalledProcessError:
        pass
