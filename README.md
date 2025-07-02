# JPMC YouTube Downloader

> A Flask-based web app to preview and download YouTube videos and audio — with support for subtitles and user-supplied cookies.

![version](https://img.shields.io/badge/version-1.0-blue)
[📘 View Changelog](./CHANGELOG.md)

## 🚀 Features

- ✅ Video/audio downloads via `yt-dlp`
- 🎚️ Resolution and format selectors
- 🗒️ Subtitle and cookie file support (WIP)
- 📊 Download history with inline progress
- 🖥️ Flask web UI with video preview

[🛣️ Roadmap](./ROADMAP.md) • [📘 Changelog](./CHANGELOG.md)

## 🔧 Notes & Known Issues

- ✔️ Confirmed working on Windows with `flask`, `yt-dlp`, and `ffmpeg` in PATH
- 💻 Executable in Codespaces and remote installs, though YouTube may detect bot-like behavior
- 📂 Cookie file upload feature implemented but not yet functional — likely related to YouTube's bot detection
- ☁️ Goal: reliable execution from cloud environments using authenticated sessions