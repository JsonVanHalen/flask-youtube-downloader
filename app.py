# app.py

from flask import Flask, render_template, request, send_file, after_this_request, jsonify
from datetime import datetime
import yt_dlp, os, glob, sqlite3, tempfile, shutil
import time
import json

app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

def log_download(info, mode, quality_or_bitrate, filename):
    """Persist download metadata, including real thumbnail URL."""
    try:
        conn = sqlite3.connect('history.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS downloads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            mode TEXT,
            quality TEXT,
            filename TEXT,
            thumbnail TEXT,
            downloaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        c.execute(
            'INSERT INTO downloads (title, url, mode, quality, filename, thumbnail) '
            'VALUES (?, ?, ?, ?, ?, ?)',
            (
                info.get('title'),
                info.get('webpage_url'),
                mode,
                quality_or_bitrate,
                filename,
                info.get('thumbnail')
            )
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"[!] Failed to log download: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url           = request.form['url'].strip()
        mode          = request.form.get('format', 'video')
        quality       = request.form.get('quality', 'best')
        audio_bitrate = request.form.get('audio_bitrate', '192')

        # 1) Create a temp directory for this download
        workdir = tempfile.mkdtemp(prefix="ytdl_")

        # 2) Choose yt-dlp format and filename suffix
        if mode == 'audio':
            fmt, suffix = 'bestaudio/best', f'_audio_{audio_bitrate}kbps'
        else:
            fmt = 'bestvideo+bestaudio/best' if quality=='best' \
                  else f"bestvideo[height<={quality}]+bestaudio/best"
            suffix = '_best' if quality=='best' else f'_{quality}p'

        # 3) Point yt-dlp at the temp directory
        outtmpl = os.path.join(workdir, f"%(title).100s{suffix}.%(ext)s")
        ydl_opts = {
            'format': fmt,
            'outtmpl': outtmpl,
            'restrictfilenames': True,
            'quiet': True
        }
        if mode == 'audio':
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': audio_bitrate
            }]

        try:
            # 4) Download into workdir
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)

            # 5) Locate the produced file
            files = glob.glob(os.path.join(workdir, '*'))
            if not files:
                raise FileNotFoundError("No file found in temp folder")
            full_path = max(files, key=os.path.getmtime)
            basename  = os.path.basename(full_path)

            # 6) Log to history (use real info so thumbnail is saved)
            log_download(info,
                         mode,
                         quality if mode=='video' else audio_bitrate,
                         basename)

            # 7) Schedule cleanup of tempdir after response
            @after_this_request
            def cleanup(response):
                try:
                    shutil.rmtree(workdir)
                except Exception:
                    pass
                return response

            # 8) Stream file back to browser
            return send_file(full_path, as_attachment=True)

        except Exception as e:
            shutil.rmtree(workdir, ignore_errors=True)
            return f"Download failed: {e}", 500

    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    url = request.form['url'].strip()
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)

        formats = info.get('formats', [])
        resolutions = sorted({
            f['height'] for f in formats
            if f.get('vcodec') != 'none' and f.get('height')
        }, reverse=True)

        return jsonify({
            'title':       info.get('title'),
            'thumbnail':   info.get('thumbnail'),
            'duration':    info.get('duration'),
            'uploader':    info.get('uploader'),
            'upload_date': info.get('upload_date'),
            'resolutions': resolutions
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/history', methods=['GET'])
def get_history():
    try:
        conn = sqlite3.connect('history.db')
        c = conn.cursor()
        c.execute("""
            SELECT title, mode, quality, downloaded_at, url, thumbnail
            FROM downloads
            ORDER BY downloaded_at DESC
            LIMIT 10
        """)
        rows = c.fetchall()
        conn.close()

        history = [{
            'title':         r[0],
            'mode':          r[1],
            'quality':       r[2],
            'downloaded_at': r[3],
            'url':           r[4],
            'thumbnail':     r[5]
        } for r in rows]

        return jsonify(history)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def batch_download_from_json(json_file='video_urls.json'):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            video_urls = data.get('videos', [])
            mode = data.get('mode', 'video')
            quality = data.get('quality', 'best')
            audio_bitrate = data.get('audio_bitrate', '192')

            for url in video_urls:
                print(f"[+] Downloading: {url}")
                # Mimic the POST behavior from index()
                with app.test_request_context(method='POST', data={
                    'url': url,
                    'format': mode,
                    'quality': quality,
                    'audio_bitrate': audio_bitrate
                }):
                    response = index()
                    print(f"[✓] Done: {url}")

    except Exception as e:
        print(f"[!] Batch download failed: {e}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'batch':
        batch_download_from_json()
    else:
        app.run(debug=True)
