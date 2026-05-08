import requests
import re
import json
import argparse
from urllib.parse import urlparse

def get_bvid(url):
    """从URL中提取B站视频的BV号"""
    parsed = urlparse(url)
    path = parsed.path
    
    # 匹配BV号格式
    bvid_re = re.compile(r'/video/(BV\w+)', re.I)
    match = bvid_re.search(path)
    if match:
        return match.group(1)
    return None

def get_video_info(bvid):
    """获取视频基本信息（标题、CID等）"""
    api_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Referer": "https://www.bilibili.com/"
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data['code'] != 0:
            print("获取视频信息失败:", data['message'])
            return None
        return data['data']
    except Exception as e:
        print("请求失败:", str(e))
        return None

def get_download_url(bvid, cid, quality=80):
    """获取视频下载地址"""
    api_url = f"https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&qn={quality}&otype=json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Referer": "https://www.bilibili.com/"
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data['code'] != 0:
            print("获取下载地址失败:", data['message'])
            return None
        return data['data']['durl'][0]['url']
    except Exception as e:
        print("请求失败:", str(e))
        return None

def download_video(url, filename):
    """下载视频文件"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Referer": "https://www.bilibili.com/"
    }
    
    try:
        with requests.get(url, headers=headers, stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("下载完成！")
        return True
    except Exception as e:
        print("下载失败:", str(e))
        return False

def main():
    parser = argparse.ArgumentParser(description='B站视频下载器')
    parser.add_argument('url', help='B站视频URL地址')
    args = parser.parse_args()

    # 获取BV号
    bvid = get_bvid(args.url)
    if not bvid:
        print("无效的B站视频URL")
        return

    # 获取视频信息
    video_info = get_video_info(bvid)
    if not video_info:
        return

    # 选择第一个分P视频
    cid = video_info['cid']
    title = video_info['title']
    print(f"正在处理视频: {title}")

    # 获取下载地址
    download_url = get_download_url(bvid, cid)
    if not download_url:
        return

    # 清理文件名中的非法字符
    clean_title = re.sub(r'[\\/:*?"<>|]', '', title)
    filename = f"{clean_title}.mp4"

    # 开始下载
    print(f"开始下载: {filename}")
    download_video(download_url, filename)

if __name__ == "__main__":
    main()