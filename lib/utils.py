from lib.colors import RED, GREEN, YELLOW, RESET

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
