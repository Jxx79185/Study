import requests

# 定义下载机器
def download_file(url, filename, headers):
    try:
        with requests.get(url, headers=headers, stream=True) as res:
            res.raise_for_status()

            # 检查内容类型
            content_type = res.headers.get('Content-Type', '')
            if 'video' not in content_type and 'audio' not in content_type:
                print(f"警告：{filename} 的内容类型可能不正确 -> {content_type}")

            # 分块下载
            total_size = 0
            with open(filename, 'wb') as f:
                for chunk in res.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        total_size += len(chunk)
            
            print(f"{filename} 下载完成，大小: {total_size} 字节")

    except Exception as e:
        print(f"下载失败: {e}")

# -------------------------------
# 实际使用机器（关键步骤！）
if __name__ == "__main__":
    # 替换成你的真实URL和Headers
    video_url='https://api.bilibili.com/x/player/wbi/playurl?qn=64&fnver=0&fnval=4048&fourk=1&avid=114029452467852&bvid=BV1RdA6eBE4o&cid=28469822280'
#获取视频链接
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
           'cookie':"buvid3=FDD03CC8-55C4-FD1D-40A2-CAFFDA17C00E13715infoc; b_nut=1739545413; _uuid=D6B10378D-DA9D-5F53-10B1C-5E4FAE7AC9A813881infoc; enable_web_push=DISABLE; enable_feed_channel=DISABLE; DedeUserID=133787074; DedeUserID__ckMd5=fa74e2a3c3202695; header_theme_version=CLOSE; rpdid=|(J|)l|~mkYl0J'u~JmlRYJ|~; buvid4=83649C48-A067-D096-ABFD-221619077BA388420-023111122-ho21%2BqF6LZpSzGHiDpgOe9m9UNeZgHT9UIz%2Bn5qCtod3CXAdyJMahA%3D%3D; buvid_fp_plain=undefined; fingerprint=673ce83b201d91b5a5ccf4208f04e347; buvid_fp=673ce83b201d91b5a5ccf4208f04e347; home_feed_column=5; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDA1ODExNjUsImlhdCI6MTc0MDMyMTkwNSwicGx0IjotMX0.B-47dQ1X8EjMQzcjd6im-Q5wIYMnKmBjpVfR__H4WXE; bili_ticket_expires=1740581105; SESSDATA=21348201%2C1755886014%2Cf5ba6%2A22CjDALKX47eYxfjxO_LoSmrzdYC31nB03ptRkTvJmS7QP1RLCjaUdFz884OLxjTzgXrQSVi05YkNjaXR5RU5YeFlzVGZ2VUNNdDQ1RHhzVHpBbjdxekhFRk56ZS1WV0tSXzdhZ0RybFFDUkZxUnZUakRsSmJKcEMzeExzQWtLS3o5SmVqXzBEaE1BIIEC; bili_jct=d772e92cb5d6f4ce62b3bebec9687626; bp_t_offset_133787074=1037481403689730048; sid=8t1f397x; CURRENT_FNVAL=4048; browser_resolution=1526-1312; b_lsid=1ED27992_1953886A316",
           'referer': 'https://www.bilibili.com/video/BV1RdA6eBE4o/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=fa19f6c3b1f9a1d266656da630e17a27'
}

    # 启动机器下载视频
    download_file(video_url, "wuming.json", headers)
    

    


