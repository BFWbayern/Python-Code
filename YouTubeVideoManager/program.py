import json

class Video:
    def __init__(self, link: str, laufzeit_sekunden: int):
        self.link = link
        self.laufzeit_sekunden = laufzeit_sekunden

class Playlist:
    def __init__(self, videos: list):
        self.videos = videos

    def playlist_ausgeben(self):
        pass # todo

    def playlist_umgedreht_ausgeben(self):
        pass # todo

    def playlist_nach_laufzeit_sortiert_ausgeben(self):
        pass # todo

    def save_to_json_file(self, filename: str):
        pass # 
    
    def gesamtlaufzeit_ermitteln(self):
        pass # todo

def main():
    # Statisch definierte Videos
    video1 = Video("https://www.youtube.com/watch?v=x7X9w_GIm1s", 143)
    video2 = Video("https://www.youtube.com/watch?v=K5KVEU3aaeQ", 7340)
    video3 = Video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", 213)

    playlist = Playlist([video1, video2, video3])

    playlist.playlist_ausgeben()
    print()

    playlist.playlist_umgedreht_ausgeben()
    print()

    playlist.playlist_nach_laufzeit_sortiert_ausgeben()
    print()

    gesamt = playlist.gesamtlaufzeit_ermitteln()
    print(f"Gesamtlaufzeit: {gesamt}")
    print()
    
    playlist.save_to_json_file("playlist.json")

if __name__ == "__main__":
    main()