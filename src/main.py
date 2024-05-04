from pytube import YouTube
from getVideo import Video

link = input("Enter a link: ")
resolution = int(input("Enter resolution [144, 240, 360, 720, 1080]: "))
path=input("Enter the path, leave blank to download to current directory: ")
Video.Download(link, resolution, path)
