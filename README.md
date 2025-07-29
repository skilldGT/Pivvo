# 📡 Pivvo

**Pivvo** is a lightweight, local-first, one-way file sharing application designed for seamless transfers between a Windows PC and devices like the Meta Quest or smartphones — all through a web browser.

---

## 🚀 Features

- 🌐 Access your PC's shared files from any device on the same network via browser
- 🔒 PIN-based access for quick, simple verification
- 🧭 Zero-install setup on receiving devices (no app required)
- 📁 Easy-to-use desktop UI with shared folder access
- ⚡ Built on Python, Flask, and PyQt5

---

## 🛠 How It Works

1. Launch `Pivvo.exe` on your Windows PC.
2. Pivvo spins up a local Flask web server.
3. You’ll see:
   - A **PIN** code for session verification
   - Your **local IP address** with port `5000` (e.g. `192.168.1.42:5000`)
4. On another device (e.g., Quest headset or phone), open the browser and visit that IP address.
5. Enter the PIN, and you'll be able to **download** the shared files.

> ⚠️ Note: File sharing is **one-way only** — devices can **download** but not upload files to your PC.

---

## 📦 Installation

1. Download the latest `Pivvo.exe` release.
2. Double-click to run — no install required.
3. The Flask server runs on `localhost:5000`.

> On first run, Windows may prompt for firewall access — allow it to enable LAN sharing.

---

## 🧩 Dependencies (if building from source)

- Python 3.10+
- Flask
- PyQt5

Install dependencies:

```bash
pip install flash pyqt5
