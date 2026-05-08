import requests
from moviepy.editor import VideoFileClip, AudioFileClip  # 修正导入

def download_file(url, filename, headers):
    try:
        with requests.get(url, headers=headers, stream=True) as res:
            res.raise_for_status()
            total_size = 0
            with open(filename, 'wb') as f:
                for chunk in res.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        total_size += len(chunk)
            print(f"{filename} 下载完成，大小: {total_size} 字节")
    except Exception as e:
        print(f"下载失败: {e}")

# 先定义 URL 和 headers
video_url = 'https://真实视频地址'
audio_url = 'https://真实音频地址'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...',
    'referer': 'https://www.bilibili.com/...'
}

# 再调用下载函数
download_file(video_url, "视频1.mp4", headers)
download_file(audio_url, "音频1.mp3", headers)

# 合并音视频
def merge_video_audio(video_path, audio_path, output_path):
    try:
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        video = video.set_audio(audio)
        video.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac",
            threads=4,
            verbose=False
        )
        print(f"合并完成: {output_path}")
    except Exception as e:
        print(f"合并失败: {e}")

merge_video_audio("视频1.mp4", "音频1.mp3", "最终视频.mp4")