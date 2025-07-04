# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [1.0.0] – 2025-07-02

### Added
- Flask-based web interface for previewing YouTube videos
- yt-dlp integration for video/audio downloading
- Resolution and format selector in the form
- Download history with progress bar and metadata
- Visual indicators for audio vs. video types
- Cookie status dashboard with live validation and freshness display
- Frontend integration for automatic refresh of cookie health after upload
- JavaScript-based cookie upload without page reload for improved UX

### Known Issues
- Cookie file upload not yet effective in bypassing YouTube rate limits
- Remote/cloud instances may encounter bot-detection barriers
