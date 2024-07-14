import os
import subprocess

def pull_latest_code():
    print("Pulling latest code from Git...")
    subprocess.run(["G:/python/期末作业/Git/bin/git.exe", "pull"])

def install_dependencies():
    print("Installing dependencies...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

def run_tests():
    print("Running tests...")
    result = subprocess.run(["python", "-m", "unittest", "discover"])
    if result.returncode != 0:
        print("Tests failed!")
        return False
    return True

def restart_web_server():
    print("Restarting web server...")
    # Assuming you're using a system service like systemd or init.d
    subprocess.run(["sudo", "service", "app.py", "restart"])

def main():
    pull_latest_code()
    install_dependencies()
    if run_tests():
        restart_web_server()
    else:
        print("Deployment failed due to test failures.")

if __name__ == "__main__":
    main()