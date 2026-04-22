from typing import Iterable, Iterator, List
import json
import copy

class Video:
    def __init__(self, id: str, title: str, url: str, description: str, thumbnail: str, created_at:str, duration_sec: int = -1):
        self.id = id
        self.title = title
        self.url = url
        self.description = description
        self.thumbnail = thumbnail
        self.created_at = created_at
        self.duration_sec = duration_sec

    def __str__(self):
        return "Videolink: " + self.url
    
class Playlist:
    def __init__(self, videos: list[Video]):
        self.videos = videos

    def __iter__(self) -> Iterator[Video]:
        return iter(self.videos)

    def __len__(self) -> int:
        return len(self.videos)

    def __getitem__(self, index: int) -> Video:
        return self.videos[index]

    def __str__(self):
        strs: list[str] = []
        for video in self.videos:
            strs.append(str(video))
        return '\n'.join(strs)
    
    def add(self, video: Video) -> None:
        self.videos.insert(0, video)

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

    def sort_created_at(self):
        self.videos.sort(key=lambda v: v.created_at, reverse=True)

    def save_to_json_file(self, filename: str):
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(to_dict(self), f, ensure_ascii=False, indent=4)

    def gesamtlaufzeit_ermitteln(self):
        gesamt = 0
        for video in self.videos:
            gesamt += video.duration_sec
        return gesamt

def to_dict(playlist: Playlist) -> dict[str, int]:
        video_dict: dict[str, int] = {}
        for video in playlist.videos:
            video_dict[video.url] = video.duration_sec
        return video_dict

def umgekehrt(videos: list[Video]) -> None:
    """
    Reverses the specified list in ref-based manner.
    
    :param videos: The list of videos to be reversed.
    :type videos: list[Video]
    """
    for i in range(len(videos)//2):
        end = len(videos)-1-i
        (videos[i], videos[end]) = (videos[end], videos[i])

def sort_laufzeit(videos: list[Video]) -> None:
    """
    Sorts the specified list in ref-based manner.
    
    :param videos: The list of videos to be sorted.
    :type videos: list[Video]
    """
    for i in range(len(videos)):
        swapped = False
        for j in range(len(videos)-i-1):
            next = j+1
            if(videos[j].duration_sec > videos[next].duration_sec):
                (videos[j], videos[next]) = (videos[next], videos[j])
                swapped = True
        if(not swapped):
            break
