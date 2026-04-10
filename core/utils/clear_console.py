import os
import subprocess

def clear_console() -> None:
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.call(command, shell=True)