from pytube import YouTube
from pytube.cli import on_progress
from pytube import extract
import subprocess
import os

class Audio:
    def audioDownload(link:str, path:str):
        yt = YouTube(link, on_progress_callback=on_progress)
        stream = yt.streams.get_audio_only()
        print(f"Title: {yt.title}")
        print(f"Meta: {yt.metadata}")
        print(f"Length: {yt.length}")
        try:
            stream.download(output_path=path)
        except:
            print("Donwload failed")
        else:
            default_name = stream.default_filename
            #change the default file name from video format (mp4) to audio frmat (mp3)
            newfile_name = default_name.replace('4','3')
            #subprocess to run command 'ffmpeg -i default_file.mp4 new_file.mp3' inside python script
            subprocess.run([
                "ffmpeg",
                '-i', os.path.join(path, default_name),
                os.path.join(path, newfile_name)
            ])
            print(f"Download completed, audio was saved in {path}")