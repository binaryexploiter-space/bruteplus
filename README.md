# 🧠 BrutePlus

**BrutePlus** is a professional CLI tool for ethical hackers, penetration testers, and CTF players.  
It automates the generation of brute-force commands for multiple services using **Hydra** and **WPScan**, and optionally runs them directly — saving time and reducing typing errors.

---

## ✨ Features

- ✅ Interactive, grouped & colorful CLI menu  
- ✅ Supports Hydra brute-forcing for:
  - SSH (22), FTP (21), HTTP/HTTPS (80/443), SMTP, RDP, VNC, POP3, IMAP, Telnet, MySQL, MSSQL, SMB, and more
- ✅ HTTP GET / POST form support with proper syntax prompts
- ✅ WPScan integration for WordPress:
  - Username enumeration with wordlists
  - Password brute-forcing for known users
- ✅ Default wordlist fallback (`/usr/share/wordlists/rockyou.txt`)
- ✅ Command history and config file auto-generation
- ✅ Clipboard auto-copy & pretty banners
- ✅ Optional: Run generated commands inside the same terminal
- ✅ Non-destructive — only generates or runs commands with your consent

---

## ⚠️ Legal Disclaimer

> **This tool is for legal and authorized security testing only.**  
> You must have **explicit permission** to scan or attack any target.  
> The developer(s) are not responsible for any misuse of this tool.

---

## 📦 Requirements

Before installing, make sure you have:
- Python 3.7+
- `hydra` installed and in your PATH
- `wpscan` installed and in your PATH

---

## 🧰 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/bruteplus.git
cd bruteplus
```
### 2️⃣ Install Python dependencies
```bash
pip3 install -r requirements.txt
```
3️⃣ Run setup

This will:

<ul><li> Copy the bruteplus binary to /usr/local/bin</li>
<li> Set it as executable for all users</li></ul>
```bash
sudo python3 setup.py install
```
After installation, you can simply run:
```bash
bruteplus
```
📄 Usage

Run the tool:
```bash
bruteplus
```
Follow the interactive menus to:

<ul><li>Generate brute force commands for Hydra or WPScan</ul>
<li>Copy them automatically to your clipboard</li>
<li>Optionally execute them right from the tool</li></ul>
Commands are also saved to ~/.bruteplus_history.
