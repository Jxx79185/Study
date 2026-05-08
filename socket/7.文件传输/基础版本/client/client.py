import socket
import struct
import json
import os

download_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'download')

def get(cli):#对服务端请求下载功能
    #第一步：先拿报头的报头
    header_h=cli.recv(4)
    #第二步：根据报头的报头发送的报头长度信息接收报头,拿到正式内容的大小
    header_size=struct.unpack('i',header_h)[0]
    header_bytes=cli.recv(header_size)
    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)
    total_size=header_dic['file_size']
    filename=header_dic['filename']
    #第三步：接收真实的数据
    file_path=os.path.join(download_path,filename)
    print(file_path)
    with open(file_path,'wb') as f:
        recv_size=0
        while recv_size<total_size:
            r_msg=cli.recv(8192)
            f.write(r_msg)
            recv_size+=len(r_msg)

    print(os.path.getsize(file_path))

def run():
    cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cli.connect(("127.0.0.1",9900))
    while True:
        #发命令
        s_msg=input('>>')
        if not s_msg:
            continue
        cli.send(s_msg.encode('utf-8'))
        if s_msg=='exit':
            print('准备断开连接')
            break

        if s_msg.split()[0]=='get':
            get(cli)
        


    cli.close() 

run()