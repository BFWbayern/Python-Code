import json
import copy

class Video:
    def __init__(self, link: str, laufzeit_sekunden: int):
        self.link = link
        self.laufzeit_sekunden = laufzeit_sekunden

    def __str__(self):
        return "Videolink: " + self.link + ", Dauer: " + str(self.laufzeit_sekunden)
    
class Playlist:
    def __init__(self, videos: list[Video]):
        self.videos = videos

    def __str__(self):
        strs: list[str] = []
        for video in self.videos:
            strs.append(str(video))
        return '\n'.join(strs)

    def playlist_ausgeben(self):
        print(self)

    def playlist_umgedreht_ausgeben(self):
        self_cpy = copy.deepcopy(self)
        # self_cpy.videos.reverse()
        umgekehrt(self_cpy.videos)
        print(self_cpy)

    def playlist_nach_laufzeit_sortiert_ausgeben(self):
        self_cpy = copy.deepcopy(self)
        # self_cpy.videos.sort(key = lambda video: video.laufzeit_sekunden)
        sort_laufzeit(self_cpy.videos)
        print(self_cpy)

    def save_to_json_file(self, filename: str):
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(to_dict(self), f, ensure_ascii=False, indent=4)

    def gesamtlaufzeit_ermitteln(self):
        gesamt = 0
        for video in self.videos:
            gesamt += video.laufzeit_sekunden
        return gesamt

def to_dict(playlist: Playlist) -> dict[str, int]:
        video_dict: dict[str, int] = {}
        for video in playlist.videos:
            video_dict[video.link] = video.laufzeit_sekunden
        return video_dict

def umgekehrt(videos: list[Video]) -> None:
    for i in range(len(videos)//2):
        end = len(videos)-1-i
        temp = videos[end]
        videos[end] = videos[i]
        videos[i] = temp

def sort_laufzeit(videos: list[Video]) -> None:
    """
    Sorts the specified list in ref-based manner.
    
    :param videos: The list of videos to be sorted.
    :type videos: list[Video]
    """
    for i in range(len(videos)):
        for j in range(len(videos)-i-1):
            temp = videos[j]
            if(videos[j].laufzeit_sekunden > videos[j+1].laufzeit_sekunden):
                videos[j] = videos[j+1]
                videos[j+1] = temp
                
def main():
    # Statisch definierte Videos
    video1 = Video("https://www.youtube.com/watch?v=x7X9w_GIm1s", 143)
    video2 = Video("https://www.youtube.com/watch?v=K5KVEU3aaeQ", 7340)
    video3 = Video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", 213)

    playlist = Playlist([video1, video2, video3])

    print("Inhalt Playlist:")
    playlist.playlist_ausgeben()
    print()

    print("Inhalt Playlist umgedreht:")
    playlist.playlist_umgedreht_ausgeben()
    print()
    
    print("Inhalt Playlist nach Laufzeit sortiert:")
    playlist.playlist_nach_laufzeit_sortiert_ausgeben()
    print()

    gesamt = playlist.gesamtlaufzeit_ermitteln()
    print(f"Gesamtlaufzeit: {gesamt}")
    print()

    playlist.save_to_json_file("YouTubeVideoManager/playlist.json")

if __name__ == "__main__":
    main()