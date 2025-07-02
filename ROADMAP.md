# 🛣️ Project Roadmap

This roadmap outlines planned features, improvements, and stretch goals for the JPMC YouTube Downloader project. It's meant to stay flexible — priorities may shift as the project evolves.

---

## ✅ Completed (v1.0.0)

- Flask-based preview UI
- yt-dlp integration for video/audio
- Format/resolution selection
- Download history panel
- Experimental cookie + subtitle file support
- Version tagging and changelog setup

---

## 🛠️ In Progress

- Fix: Make cookie upload functional from client to yt-dlp backend
- Add: Basic error handling and user-friendly error messages
- Polish: Improve layout/UI and mobile responsiveness

---

## 🧭 Next Goals (v1.1.0 Target)

- ✅ Run headless from Codespace or cloud reliably
- ☁️ Add support for persistent cloud-authentication (via stored cookies or OAuth2?)
- 🧪 Add unit tests for core functions (e.g., `download_video()`)
- 🚀 Dockerize the app with environment-based config
- 🔒 Add auth for shared/multi-user deployment
- ✨ Enable auto-subtitle generation via Whisper (stretch)

---

## 💡 Ideas & Stretch Goals

- Streamable preview of content before download
- Custom output template selection (filename control)
- Support for other platforms (e.g., Vimeo, SoundCloud)
- Usage stats dashboard (downloads, formats, etc.)