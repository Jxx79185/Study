import os
import json
import requests
import subprocess
from urllib.parse import urlparse, parse_qs
from typing import Dict, List, Optional

class BiliVideoDownloader:
    def __init__(self, bvid: str, cookie: str, quality: int = 80):
        """
        B站视频下载工具
        
        参数：
        - bvid: 视频BV号（如"BV1RdA6eBE4o"）
        - cookie: 登录后的Cookie字符串
        - quality: 视频清晰度（默认80=1080P）
        """
        self.bvid = bvid
        self.cookie = cookie
        self.quality = quality
        self.cid = None  # 视频分P的ID
        self.base_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": f"https://www.bilibili.com/video/{self.bvid}",
            "Cookie": self.cookie
        }

    def _get_cid(self) -> str:
        """获取视频分P的CID"""
        api_url = f"https://api.bilibili.com/x/web-interface/view?bvid={self.bvid}"
        try:
            response = requests.get(api_url, headers=self.base_headers)
            response.raise_for_status()
            data = response.json()
            if data["code"] != 0:
                raise ValueError(f"获取CID失败: {data.get('message')}")
            self.cid = data["data"]["pages"][0]["cid"]
            return self.cid
        except Exception as e:
            raise RuntimeError(f"CID获取异常: {str(e)}")

    def _get_play_urls(self) -> Dict:
        """获取视频播放地址信息"""
        if not self.cid:
            self._get_cid()

        params = {
            "bvid": self.bvid,
            "cid": self.cid,
            "qn": self.quality,
            "fnval": 4048,  # 启用DASH格式
            "fourk": 1
        }

        try:
            response = requests.get(
                "https://api.bilibili.com/x/player/wbi/playurl",
                params=params,
                headers=self.base_headers
            )
            response.raise_for_status()
            data = response.json()
            if data["code"] != 0:
                raise ValueError(f"接口返回错误: {data.get('message')}")
            return data["data"]
        except Exception as e:
            raise RuntimeError(f"播放地址获取失败: {str(e)}")

    @staticmethod
    def _download_file(url: str, filename: str, headers: Dict) -> None:
        """分块下载文件"""
        try:
            with requests.get(url, headers=headers, stream=True) as res:
                res.raise_for_status()
                with open(filename, "wb") as f:
                    for chunk in res.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            print(f"✅ 下载完成: {filename} ({os.path.getsize(filename)//1024}KB)")
        except Exception as e:
            raise RuntimeError(f"下载失败: {str(e)}")

    def _merge_media(self, video_path: str, audio_path: str, output_path: str) -> None:
        """合并音视频"""
        try:
            subprocess.run([
                "ffmpeg", "-y",
                "-i", video_path,
                "-i", audio_path,
                "-c:v", "copy",
                "-c:a", "copy",
                output_path
            ], check=True)
            print(f"🎉 合并完成: {output_path}")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"合并失败: {str(e)}")

    def auto_download(self, output_name: str = "output.mp4") -> None:
        """全自动下载流程"""
        try:
            # Step 1: 获取元数据
            play_data = self._get_play_urls()
            dash_data = play_data["dash"]

            # Step 2: 获取最佳质量的音视频地址
            video_info = max(
                dash_data["video"], 
                key=lambda x: x.get("width", 0) * x.get("height", 0)
            )
            audio_info = max(
                dash_data["audio"], 
                key=lambda x: x.get("bandwidth", 0)
            )

            video_url = video_info["base_url"]
            audio_url = audio_info["base_url"]

            # Step 3: 下载文件
            print("⏳ 开始下载视频分片...")
            self._download_file(video_url, "temp_video.m4s", self.base_headers)
            
            print("⏳ 开始下载音频分片...")
            self._download_file(audio_url, "temp_audio.m4s", self.base_headers)

            # Step 4: 合并文件
            print("⏳ 合并音视频...")
            self._merge_media("temp_video.m4s", "temp_audio.m4s", output_name)

            # 清理临时文件
            os.remove("temp_video.m4s")
            os.remove("temp_audio.m4s")
            print("🧹 临时文件已清理")

        except Exception as e:
            print(f"❌ 发生错误: {str(e)}")
            if os.path.exists("temp_video.m4s"):
                os.remove("temp_video.m4s")
            if os.path.exists("temp_audio.m4s"):
                os.remove("temp_audio.m4s")
            raise

if __name__ == "__main__":
    # 使用示例 ============================================
    # 获取Cookie方法：
    # 1. 登录B站后按F12打开开发者工具
    # 2. 进入Network(网络)面板
    # 3. 刷新页面，点击任意请求，复制Request Headers中的Cookie值

    downloader = BiliVideoDownloader(
        bvid="BV1LjsWe2Eod",  # 替换为目标视频BV号
        cookie="buvid3=FDD03CC8-55C4-FD1D-40A2-CAFFDA17C00E13715infoc; b_nut=1739545413; _uuid=D6B10378D-DA9D-5F53-10B1C-5E4FAE7AC9A813881infoc; enable_web_push=DISABLE; enable_feed_channel=DISABLE; DedeUserID=133787074; DedeUserID__ckMd5=fa74e2a3c3202695; header_theme_version=CLOSE; rpdid=|(J|)l|~mkYl0J'u~JmlRYJ|~; buvid4=83649C48-A067-D096-ABFD-221619077BA388420-023111122-ho21%2BqF6LZpSzGHiDpgOe9m9UNeZgHT9UIz%2Bn5qCtod3CXAdyJMahA%3D%3D; buvid_fp_plain=undefined; fingerprint=673ce83b201d91b5a5ccf4208f04e347; home_feed_column=5; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDA4Mzg1NjAsImlhdCI6MTc0MDU3OTMwMCwicGx0IjotMX0.9VR8u9ZlIpQKUEZpUbRpl6TpA8IpyfUv5BE4RqXCeXA; bili_ticket_expires=1740838500; SESSDATA=daf7e97c%2C1756145225%2C211ed%2A22CjCpktbKtj4hkEKRkCp8m4vSjn1Q9tHmxgkWVl6FZu5EV7--hysQ28cAOcHkf2PWfckSVkZhZTRJdXp4UlNmRGNOcEtqdE9pQ3FVTlFhRDZIUWlDSDdNVDJwR0Rvdy1sTW9oV0w3aTg1SENvWnJ4T0szQ25uSEVBZm9lQVJSekZVOE5CZkt1cTVnIIEC; bili_jct=40d7a360ef26b681e2ac2832a5757d79; LIVE_BUVID=AUTO9817406586465324; PVID=5; b_lsid=4E1EE7BE_1954C660AFA; browser_resolution=1526-1312; sid=8rh3gabx; bp_t_offset_133787074=1038974647854432256; CURRENT_FNVAL=4048; buvid_fp=673ce83b201d91b5a5ccf4208f04e347; CURRENT_QUALITY=116",  # 替换为你的Cookie
        quality=80  # 清晰度选择（80=1080P）
    )

    try:
        downloader.auto_download("打完.mp4")
    except Exception as e:
        print(f"❗ 程序运行失败: {str(e)}")