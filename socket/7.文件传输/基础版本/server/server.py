import socket
import struct
import json
import os

download_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'genshin')
def get(con,data):#对客户端下载请求回应功能
    filename=data[1] 
    #执行命令,并且拿到执行的结果
    #第一步：制作固定长度的报头的报头
    file_path=os.path.join(download_path,filename)
    header_dic={'filename':filename,
                'md5':'xxdxxx',
                'file_size':os.path.getsize(file_path)}      
    header_json=json.dumps(header_dic)
    header_bytes=header_json.encode('utf-8')
    header_h=struct.pack('i',len(header_bytes))#报头的报头
    print(header_h)
    con.send(header_h) #发送报头的报头   
    #第二步：把报头先发送给客户端
    con.send(header_bytes)
    #返回结果
    #第二步：再发真实的内容
    Chunk_Size=8192
    
    with open(file_path,'rb') as f:     
        while True:
            Chunk=f.read(Chunk_Size)
            if not Chunk:
                break
            con.send(Chunk)     
    print(f'已发送字节长度为{os.path.getsize(file_path)}的文件')

def run():

    ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ser.bind(('127.0.0.1',9900))
    ser.listen(1)

    while True:
        con,cli_addr=ser.accept()
        print(cli_addr)
        while True:
            try:
                #收命令
                data=con.recv(1024).decode('utf-8').split()
                print(f'对方发送信息：{data}')
                if data=='exit':
                    print('对方准备断开链接')
                    break
                if data[0]=='get':
                    get(con,data)
                
            except ConnectionResetError as e:
                print(e)
                break
        con.close()

run()