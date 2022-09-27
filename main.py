"""
Use a playlist to stream files from m3u8: https://github.com/globocom/m3u8
    pip install m3u8
Example from Akamai:
https://learn.akamai.com/en-us/webhelp/media-services-live/media-services-live-4-user-guide/GUID-0A50253F-0B1B-406B-A8C9-3788CB42F950.html
"""

from pathlib import Path
import pylivestream.api as pls

import m3u8

playlist_m3u8 = Path(__file__).parent / "local.m3u8"
key = Path(__file__).parent / "youtube.key"


playlist = m3u8.load(str(playlist_m3u8))

files = playlist.files

sites = ["youtube"]
urlm = "rtmp://a.rtmp.youtube.com/live2"
# while True:
for file in files:
    pls.stream_file(
        loop=True,
        ini_file=key,
        websites=sites,
        assume_yes=True,
        video_file=file,
    )