# 🧰 WSL Dev Environment Setup Guide

This quickstart sets up a full-stack development environment using WSL, VS Code, and GitHub SSH. Designed for fast bootstraps on fresh Windows machines.

---

## 1️⃣ Install Core Tools

### ✅ WSL (Ubuntu)
Open PowerShell (Admin):

```powershell
wsl --install

---

# 🚀 Daily Dev Launch Guide (WSL Native Workflow)

A step-by-step routine to wipe and reboot your Flask dev environment from scratch each day. Builds repeatable muscle memory and ensures a clean, frictionless start.

## ✅ Launch Checklist

| Step | Command / Action                                      | Notes |
|------|--------------------------------------------------------|-------|
| 1️⃣  | Open WSL terminal                                      | From Windows Terminal or Start menu |
| 2️⃣  | `rm -rf ~/flask-youtube-downloader`                    | Deletes previous clone |
| 3️⃣  | `git clone git@github.com:jasonvanhalen/flask-youtube-downloader.git` | Pull fresh project |
| 4️⃣  | `cd flask-youtube-downloader` → `code .` OR launch workspace file | Opens VS Code scoped to project |
| 5️⃣  | VS Code → Terminal → New Terminal                      | Should be WSL (`jason@ubuntu`) |
| 6️⃣  | Dev 🚀                                                 | Run Flask, write code, commit updates |

---

## 🧠 Visual Flow: Clean Slate to Coding

```plaintext
┌────────────────────────────┐
│ 1. Open WSL Terminal       │
└────────────┬───────────────┘
             ↓
┌────────────────────────────┐
│ 2. Delete Old Clone        │
│    rm -rf ~/flask...       │
└────────────┬───────────────┘
             ↓
┌────────────────────────────┐
│ 3. Clone Repo Fresh        │
│    git clone ...           │
└────────────┬───────────────┘
             ↓
┌────────────────────────────┐
│ 4. Open VS Code            │
│    code . or workspace     │
└────────────┬───────────────┘
             ↓
┌────────────────────────────┐
│ 5. Open WSL Terminal       │
│    Ready to dev            │
└────────────┬───────────────┘
             ↓
┌────────────────────────────┐
│ 6. Run, build, commit 🚀   │
└────────────────────────────┘

---

# 🧪 Project Execution Workflow

After setting up your workspace and activating the virtual environment, follow these steps to run the application or test scripts.

## ✅ Virtual Environment Setup

1. Create a new virtual environment:

   ```bash
   python3 -m venv venv
