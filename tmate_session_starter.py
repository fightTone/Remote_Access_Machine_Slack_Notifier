import subprocess
import time

def run_command(cmd):
    return subprocess.check_output(cmd, shell=True, text=True)

def get_ssh_connection_string():
    run_command("tmate -S /tmp/tmate.sock new-session -d")
    run_command("tmate -S /tmp/tmate.sock wait tmate-ready")

    ssh_session = run_command("tmate -S /tmp/tmate.sock display -p '#{tmate_ssh}'")
    web_session = run_command("tmate -S /tmp/tmate.sock display -p '#{tmate_web}'")
    ssh_session_read_only = run_command("tmate -S /tmp/tmate.sock display -p '#{tmate_ssh_ro}'")
    web_session_read_only = run_command("tmate -S /tmp/tmate.sock display -p '#{tmate_web_ro}'")
    output = f"SSH: {ssh_session}\nWeb: {web_session}\nSSH RO: {ssh_session_read_only}\nWeb RO: {web_session_read_only}"
    # print(output)
    return output

if __name__ == "__main__":
    get_ssh_connection_string()