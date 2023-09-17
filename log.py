from termcolor import colored, cprint

def info(msg):
    print(
        colored(f"[INFO]", 'blue', 'on_blue') + ' ' +
        colored(f"{msg}")
    )

def warn(msg):
    print(
        colored(f"[WARN]", 'yellow', 'on_yellow') + ' ' +
        colored(f"{msg}")
    )

def error(msg):
    print(
        colored(f"[ERROR]", 'red', 'on_red') + ' ' +
        colored(f"{msg}")
    )