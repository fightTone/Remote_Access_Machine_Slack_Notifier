import os
import subprocess
import getpass


def run_command(cmd):
    return subprocess.check_output("wsl " + cmd, shell=True, text=True)

username = getpass.getuser()
#edit the path where you have the bot.py file
output = run_command(f"python3 /mnt/c/Users/{username}/Works/playground/slack_notifier/bot.py")
print(output)