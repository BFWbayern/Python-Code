from flask import Flask, render_template, request, redirect, url_for, abort
from flask import make_response
import json, os, re
from datetime import datetime
from yt_video import Video, Playlist

def load_playlist() -> Playlist:
    if not os.path.exists(PLAYLIST_PATH):
        save_playlist(Playlist([]))

    try:
        with open(PLAYLIST_PATH, 'r', encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Invalid playlist format")
    except Exception:
        save_playlist(Playlist([]))
        data = []

    videos = []
    for entry in data:
        if not entry: 
            continue
        videos.append(Video(
            id=entry["id"],
            title=entry["title"],
            url=entry["url"],
            description=entry["description"],
            thumbnail=entry["thumbnail"],
            created_at=entry["created_at"],
            duration_sec=entry["duration_sec"],
        ))

    return Playlist(videos)

def save_playlist(playlist: Playlist):
    with open(PLAYLIST_PATH, 'w', encoding="utf-8") as f:
        json.dump(to_dict(playlist), f, ensure_ascii=False, indent=2)

def to_dict(playlist: Playlist) -> list[dict]:
        video_dict: list[dict] = []
        for video in playlist:
            entry = {
                "id": video.id,
                "title": video.title,
                "url": video.url,
                "description": video.description,
                "thumbnail": video.thumbnail,
                "created_at": video.created_at,
                "duration_sec": video.duration_sec
            }
            video_dict.append(entry)
        return video_dict

PLAYLIST_PATH = os.path.join(os.path.dirname(__file__), "data", "playlist.json")
YOUTUBE_PATTERNS = [
    r"(?:https?://)?(?:www\.)?youtu\.be/([A-Za-z0-9_-]{11})",
    r"(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([A-Za-z0-9_-]{11})",
    r"(?:https?://)?(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]{11})",
    r"(?:https?://)?(?:www\.)?youtube\.com/shorts/([A-Za-z0-9_-]{11})",
]

app = Flask(__name__)

os.makedirs(os.path.dirname(PLAYLIST_PATH), exist_ok=True)

def extract_youtube_id(url: str):
    url = (url or "").strip()
    for pattern in YOUTUBE_PATTERNS:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", url):
        return url
    return None

def build_thumbnail(yt_id: str):
    return f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"

@app.route('/', methods=["GET"])
def index():
    playlist = load_playlist()
    playlist.sort_created_at()
    return render_template("index.html", playlist=playlist)

@app.route("/videos", methods=["POST"])
def add_video():
    title = (request.form.get("title") or "").strip()
    url = (request.form.get("url") or "").strip()
    desc = (request.form.get("description") or "").strip()

    if not title or not url:
        return _bad_request("Please provide both Title and YouTube URL.")

    id = extract_youtube_id(url)
    if not id:
        return _bad_request("Invalid YouTube URL or ID.")

    playlist = load_playlist()
    video: Video = Video(
        id=id,
        title=title,
        url=f"https://www.youtube.com/watch?v={id}",
        description=desc,
        thumbnail=build_thumbnail(id),
        created_at=datetime.now().isoformat(),
        duration_sec=-1
    )
    
    if any(v.id == id for v in playlist):
        return _bad_request("Dieses YouTube-Video ist bereits gespeichert.")
    
    playlist.add(video)
    save_playlist(playlist)

    if request.headers.get("HX-Request") == "true":
        return render_template("partials/video_card.html", video=video), 201

    return redirect(url_for("index"))

@app.route("/videos/<video_id>/edit", methods=["GET"])
def edit_video(video_id):
    playlist = load_playlist()
    video = next((v for v in playlist if v.id == video_id), None)
    if not video:
        abort(404)
    return render_template("partials/edit_form.html", video=video)

@app.route("/videos/<video_id>/update", methods=["POST"])
def update_video(video_id):
    playlist = load_playlist()
    video = next((v for v in playlist if v.id == video_id), None)
    if not video:
        abort(404)

    video.title = request.form.get("title", "").strip()
    video.description = request.form.get("description", "").strip()

    save_playlist(playlist)

    return '<script>window.location.reload()</script>', 200


@app.route("/videos/<video_id>/delete", methods=["POST"])
def delete_video(video_id):
    playlist = load_playlist()

    new_playlist = Playlist([v for v in playlist if v.id != video_id])

    if len(new_playlist) == len(playlist):
        abort(404)

    save_playlist(new_playlist)

    return '<script>window.location.reload()</script>', 200


def _bad_request(message: str):
    if request.headers.get("HX-Request") == "true":
        resp = make_response(message, 400)
        return resp
    
    return make_response(f"Bad Request: {message}", 400)

if __name__ == "__main__":
    app.run(debug=True)
