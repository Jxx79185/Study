import socket
import time
import struct
import json
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
    
    #第一步：先拿报头的报头
    header_h=cli.recv(4)
    #第二步：根据报头的报头发送的报头长度信息接收报头,拿到正式内容的大小
    header_size=struct.unpack('i',header_h)[0]
    header_bytes=cli.recv(header_size)
    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)
    total_size=header_dic['total_size']
    #第三步：接收真实的数据
    recv_size=0
    recv_data=b''
    while recv_size<total_size:

        r_msg=cli.recv(1024)
        recv_data+=r_msg
        recv_size+=len(r_msg)

    print(len(recv_data))
    print(recv_data.decode('gbk'))

cli.close() 