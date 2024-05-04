import argparse
from pytube import YouTube
from getVideo import Video
from getAudio import Audio

parent_directory = r"/home/agdfl/Downloads"

parser = argparse.ArgumentParser(prog="Youloader",
                                                    description="A youtube video downloader",
                                                      )
parser.add_argument("-v", "--video",metavar="string" , type=str, help="Download under video format with given link, by default it will download video with highest resolution unless specified otherwise, see --video-resolution for more info")
parser.add_argument("-r", "--resolution", metavar="N", choices=[144, 240, 360, 720, 1080], default=360, type=int, help="Choose the resolution type of video")
parser.add_argument("-p", "--path", metavar="string", default=parent_directory, help="Specify where the file is downloaded to, default to $HOME/Videos. If the folder doesn't existed, it will be created")
parser.add_argument("-a", "--audio", metavar="string", type=str, help="Download file under audio format")
args = parser.parse_args()                                                                                     

if __name__=="__main__":
    if args.video:
       Video.defaultDownload(args.video, args.resolution, args.path)
    elif args.audio:
        Audio.audioDownload(args.audio, args.path)
       