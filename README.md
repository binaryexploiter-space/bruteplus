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
