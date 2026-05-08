import requests

def download_file(url, filename, headers):
    url="地址"
    headers={'user-agent':"...",'cookie':"...",'Referer':"..."}
    res=requests.get(url,headers=headers,stream=True)

    with open(filename,'wb') as f:
        for chunk in res.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
        
    print(f"{filename} 下载完成，大小: {len(res.content)} 字节")






    