# JVH YouTube Downloader

> Note, I've temporarily abandoned this branch, might revisit later but am content with local exectution for now. A Flask-based web app to preview and download YouTube videos and audio — with support for subtitles and cookie-based authentication diagnostics.

![version](https://img.shields.io/badge/version-1.0-blue)
[📘 View Changelog](./CHANGELOG.md)

## 🚀 Features

- ✅ Video/audio downloads via `yt-dlp`
- 🎚️ Resolution and format selectors
- 📊 Actionable Download history
- 🖥️ Flask web UI with video preview
- 🍪 Cookie status dashboard with validation and freshness indicators

[🛣️ Roadmap](./ROADMAP.md) • [📘 Changelog](./CHANGELOG.md)

## 🔧 Notes & Known Issues

- ✔️ Confirmed working on Windows with `flask`, `yt-dlp`, and `ffmpeg` in PATH
- 💻 Executable in Codespaces and remote installs, though YouTube may detect bot-like behavior
- 🍪 Cookie file upload and validation system functions as intended
- ❌ YouTube may still block requests from cloud environments despite valid cookies
- ☁️ Goal: reliable execution from cloud environments using authenticated sessions

## 🧠 Cookie Behavior

This branch includes a working cookie upload and validation system.  
However, YouTube may block requests from remote/cloud environments due to bot-detection mechanisms.  
Local execution with browser-integrated cookies is recommended for best results.
