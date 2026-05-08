import ffmpeg

import subprocess

# 下载 HLS 视频流
command = [
    'ffmpeg',
    '-i', 'https://hackeyouxuanedu.edu.gzfeice.com/stream.m3u8',
    '-c', 'copy',
    'output.mp4'
]
subprocess.run(command)