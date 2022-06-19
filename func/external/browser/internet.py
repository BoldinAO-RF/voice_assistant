import subprocess

def check_is_up():
    try:
        subprocess.check_call(["ping", "8.8.8.8", "-n", "1"])
        return True
    except subprocess.CalledProcessError:
        return False