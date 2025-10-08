#!/usr/bin/env python3
import os
import subprocess
import shutil
import sys

def install_requirements():
    req_file = "requirements.txt"
    if os.path.exists(req_file):
        print("[*] Installing Python dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_file], check=True)
    else:
        print("[*] No requirements.txt found. Skipping dependency installation.")

def move_binary():
    binary_name = "bruteplus"  # The script in current directory
    src_path = os.path.join(os.getcwd(), binary_name)
    dest_path = f"/usr/local/bin/{binary_name}"

    if not os.path.exists(src_path):
        print(f"[!] {binary_name} not found in current directory.")
        sys.exit(1)

    print(f"[*] Moving {binary_name} to /usr/local/bin ...")
    shutil.copy(src_path, dest_path)

    print("[*] Setting executable permissions...")
    subprocess.run(["chmod", "777", dest_path], check=True)

    print(f"[+] Installed successfully! You can now run: {binary_name}")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[!] Please run this script with sudo.")
        sys.exit(1)

    install_requirements()
    move_binary()
