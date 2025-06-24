---

````markdown
# 🔍 Enhanced Log Seeker

**Enhanced Log Seeker** is a modern Python GUI tool designed for analyzing log files from Android ROM and kernel build processes. With smart detection and a clean interface, it helps developers quickly identify critical issues in logs.

![screenshot](https://i.imgur.com/your_screenshot.png) <!-- Replace with actual screenshot URL -->

---

## ✨ Features

- 🚨 **Smart Detection** of over 20+ issue categories:
  - Kernel errors, SELinux violations, GApps failures, Soong/Ninja build issues, and more.
- 🌒 **Modern Dark Theme** inspired by Orchis GTK
- 📊 **Real-time Statistics** with severity-level breakdown
- 🔍 **Filter by Issue Level** (ERROR, WARNING, INFO, etc.)
- ⚡ **Context-aware Analysis** for Android ROM logs
- 🖱️ **Right-click Menu** for copying, searching similar logs
- 💾 **Export Results** to `.txt` or clipboard
- ⌨️ **Keyboard Shortcuts**:
  - `Ctrl+O`: Open File
  - `Ctrl+R` / `F5`: Run Analysis
  - `Ctrl+S`: Export Report
  - `Ctrl+Q`: Exit App

---

## 🚀 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/idovpn1321/Log.git
cd Log
````

### 2. Run the App

```bash
python3 run.py
```

> Make sure you're using **Python 3.6+**

---

## 📂 Supported File Types

* `.log`, `.txt`, `.py`, `.mk`, and `.rc` files
* Build logs from:

  * AOSP / LineageOS / GKI / KernelSU
  * `repo sync`, `make`, `ninja`, etc.
* Generic Android logs (e.g., `logcat`, `dmesg`)

---

## 🧠 Log Detection System

Each line is scanned with advanced pattern matching and keyword detection.
Examples of recognized patterns:

* `fatal error: missing file`
* `selinux denied`
* `undefined reference`
* `ninja: build stopped`
* `make: *** [target] Error`

---

## 📁 Project Structure

```
.
├── run.py                   # Main GUI application
├── rom_detection_levels.py  # Android-specific log analysis engine
├── README.md
```

---

## 👨‍💻 Developer

* **Author:** [@idovpn1321 (Zuan)](https://github.com/idovpn1321)
* **Contributions:** Pull requests are welcome!

---

## 📸 Screenshots

> Upload a screenshot and replace the placeholder link above with your image.

---

## ☕ Support

This project was built with passion (and late nights of debugging Android logs).
If it helps you, feel free to give it a ⭐️ or [share your feedback](https://github.com/idovpn1321/Log/issues)!

---

## 📜 License

MIT License — free for personal or commercial use.
Fork it, improve it, share it. Just don’t forget to credit 😉
