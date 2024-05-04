from pytube.cli import on_progress
from pytube import Stream
from tqdm.auto import tqdm
from time import sleep

def progress(stream: Stream, chunk: bytes, bytes_remaining: int):
    filesize = stream.filesize
    i = 0
    for i in tqdm(range(filesize)):
        i += (filesize-bytes_remaining)/filesize