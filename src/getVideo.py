import re
from progressBar import progress
from pytube import YouTube
from pytube.cli import on_progress
from pytube.exceptions import VideoUnavailable
from pytube.exceptions import VideoRegionBlocked

class Video:
    def defaultDownload(link: str, resolution_type: int, path: str):
        yt = YouTube(link, on_progress_callback=progress)
        stream = yt.streams.get_by_resolution(resolution_type)
        print(f"Title: {yt.title}")
        print(f"Meta: {yt.metadata}")
        print(f"Length: {yt.length}")
        try:
            stream.download(output_path=path)
        except VideoUnavailable:
            print("Error while downloading. Download aborted")
        else:
            print(f"Download completed, video was saved in {path}")