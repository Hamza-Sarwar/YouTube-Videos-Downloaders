import os
import subprocess

import pytube

yt = pytube.YouTube("VIDEO'S URL")

vids = yt.streams
for i in range(len(vids)):
    print(i, '. ', vids[5])

vnum = int(input("Enter vid num: "))

parent_dir = r"C:\YTDownloads"
vids[vnum].download(parent_dir)

new_filename = input("Enter filename (including extension): ")  # e.g. new_filename.mp3

default_filename = vids[vnum].default_filename  # get default name using pytube API
subprocess.run([
    'ffmpeg',
    '-i', os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('done')
