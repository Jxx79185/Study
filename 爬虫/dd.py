import requests
import re

# 网址接口
url1 = 'https://api.bilibili.com/x/player/wbi/playurl?qn=80&fnver=0&fnval=4048&fourk=1&avid=114051078164233&bvid=BV1EoA2ewEqw&cid=28532343850'
# 伪装浏览器数据
wz = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
      'cookie':"buvid3=FDD03CC8-55C4-FD1D-40A2-CAFFDA17C00E13715infoc; b_nut=1739545413; _uuid=D6B10378D-DA9D-5F53-10B1C-5E4FAE7AC9A813881infoc; enable_web_push=DISABLE; enable_feed_channel=DISABLE; DedeUserID=133787074; DedeUserID__ckMd5=fa74e2a3c3202695; header_theme_version=CLOSE; rpdid=|(J|)l|~mkYl0J'u~JmlRYJ|~; buvid4=83649C48-A067-D096-ABFD-221619077BA388420-023111122-ho21%2BqF6LZpSzGHiDpgOe9m9UNeZgHT9UIz%2Bn5qCtod3CXAdyJMahA%3D%3D; buvid_fp_plain=undefined; fingerprint=673ce83b201d91b5a5ccf4208f04e347; buvid_fp=673ce83b201d91b5a5ccf4208f04e347; home_feed_column=5; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDA1ODExNjUsImlhdCI6MTc0MDMyMTkwNSwicGx0IjotMX0.B-47dQ1X8EjMQzcjd6im-Q5wIYMnKmBjpVfR__H4WXE; bili_ticket_expires=1740581105; SESSDATA=21348201%2C1755886014%2Cf5ba6%2A22CjDALKX47eYxfjxO_LoSmrzdYC31nB03ptRkTvJmS7QP1RLCjaUdFz884OLxjTzgXrQSVi05YkNjaXR5RU5YeFlzVGZ2VUNNdDQ1RHhzVHpBbjdxekhFRk56ZS1WV0tSXzdhZ0RybFFDUkZxUnZUakRsSmJKcEMzeExzQWtLS3o5SmVqXzBEaE1BIIEC; bili_jct=d772e92cb5d6f4ce62b3bebec9687626; CURRENT_QUALITY=80; sid=7xqf1y6f; bp_t_offset_133787074=1037750891412717568; browser_resolution=1526-1312; b_lsid=27662D9E_1953C644B59; CURRENT_FNVAL=4048",
      'Referer':'https://www.bilibili.com/video/BV1EoA2ewEqw/?spm_id_from=333.1007.tianma.1-2-2.click&vd_source=fa19f6c3b1f9a1d266656da630e17a27'}

episodenumber = 0
while True:
    # 参数列表 在负载里面去复制过来
    data = ('qn=80&fnver=0&fnval=4048&fourk=1&avid=114051078164233&bvid=BV1EoA2ewEqw&cid=28532343850')
    # 请求的时候用post 网址接口 和 参数列表分别填进去
    res1 = requests.post(url1, json=data, headers=wz)

    # 从res1.text里面去把视频的链接单独提取出来！
    video_url = re.findall('"photoUrl":"(.*?)","photoH265Url"', res1.text)[0]
    print(video_url)

    # 把前面得到的视频链接带入下面的3行代码。
    url = video_url
    res = requests.get(url)
    open(f'我的小娇妻第{episodenumber+1}集.mp4', 'wb').write(res.content)
    episodenumber += 1