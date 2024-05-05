Youloader

A youtube video downloader using python with pytube library

usage: Youloader [-h] [-v string] [-r N] [-p string] [-a string]


A youtube video downloader


options:

  -h,   --help                  show this help message and exit
  
  -v string,   --video string
  
                                Download under mp4 format with given link, by
                                default it will download video with highest resolution
                                unless specified otherwise, see --video-resolution for
                                more info
  
  -r N,     --resolution N      
  
  Choose the resolution type of video. Pick one of the following 144, 240, 
                                360, 720.
  
  -p string,   --path string
                                
                                Specify where the file is downloaded to, default to
                                $HOME/Videos. If the folder doesn't existed, it will
                                be created
  
  -a string,    --audio string
                                
                                Download file under mp3 format. ffmpeg is required
