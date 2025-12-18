# ProperBT – Kali Linux Bluetooth Manager

A Kali Linux–native Bluetooth management tool designed to make connecting and managing external Bluetooth devices simple, reliable, and beginner-friendly — while behaving like a built-in Kali tool.

---

## 🚀 Features

- Works on **ALL Kali Linux versions**
  - Kali Rolling
  - Kali Stable
  - Kali Light
  - Kali NetHunter Desktop
- Detects **internal & external USB Bluetooth adapters**
- Menu-based **CLI interface** (works on minimal installs)
- Scan, pair, trust, connect, disconnect, and remove devices
- Automatically enables Bluetooth services if disabled
- Handles common issues:
  - `rfkill` blocked Bluetooth
  - Adapter not found
  - Bluetooth service stopped
- Local logging for debugging
- No exploitation or hacking features

---

## 📦 Clone & Run (Like Native Kali Tools)

```bash
git clone https://github.com/Prabesh-Proper/ProperBT.git
cd ProperBT
sudo ./properbt
```

Or install system-wide:

```bash
sudo bash install.sh
sudo properbt
```

No configuration required.  
Clone → Run → Works.

---

## 🛠 Dependencies

The tool automatically checks for required packages:

- `bluez`
- `bluetoothctl`
- `rfkill`
- `systemctl`
- `python3`

If any dependency is missing, ProperBT will suggest install commands.

---

## 📁 Project Structure

```
ProperBT/
├── properbt
├── install.sh
├── requirements.txt
├── src/
├── logs/
├── docs/
├── LICENSE
└── README.md
```

---

## 🔐 Security & Ethics

- ❌ No Bluetooth hacking
- ❌ No sniffing or MITM attacks
- ❌ No unauthorized access
- ✅ Least-privilege execution
- ✅ Fully legal & ethical usage

---

## 👤 Author & Copyright

**Made by Proper**

Copyright © Proper  
GitHub: https://github.com/Prabesh-Proper

All rights reserved.

---

## 📜 License

MIT License (see LICENSE file)

---

> Built for Kali. Built by Proper.
