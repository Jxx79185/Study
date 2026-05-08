import requests
url = 'ffmpeg -i "https://haokeyouxuanedu.edu.gzfeice.com/stream.m3u8" -c copy video.mp4'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Referer": "https://haokeyouxuanedu.edu.gzfeice.com/",
}

res=requests.get(url,headers=headers)
print(res.status_code)
open ('视频3.mp4','wb').write(res.content)
