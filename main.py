import os
import ssl
from pathlib import Path
import pylivestream.api as pls
from pytube import YouTube, Playlist


def start():
  ssl._create_default_https_context = ssl._create_unverified_context
  playlist_string = 'https://youtube.com/playlist?list=OLAK5uy_mDWtgeNF9LzujhjNi5DFcX-Lld0_ZMr_s'
  urlm = "rtmp://a.rtmp.youtube.com/live2"
  key = Path(__file__).parent / "youtube.key"

  playlist = Playlist(playlist_string)
  print("start....")
  sites = ["youtube"]
  while True:
    for video in playlist.videos:
        videofile = video.streams.get_highest_resolution().download()
        print("stream....")
        pls.stream_file(
            ini_file=key,
            websites=sites,
            assume_yes=True,
            video_file=videofile,
        )

if __name__ == "__main__":
  start()