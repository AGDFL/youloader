from pytube import YouTube
from pytube.exceptions import VideoUnavailable

class Video:
    def Download(link: str, resolution_type: int, path:str) :
        yt = YouTube(link)
        stream = yt.streams.get_by_resolution(resolution_type)
        try:
            print(f"Video title: {yt.title}")
            print(f"Video resolution: {resolution_type}")
            stream.download(path)
        except VideoUnavailable:
            print("Unable to download video")
        else:
            print("Download successfully")
