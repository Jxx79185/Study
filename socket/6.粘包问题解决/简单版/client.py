import socket
import time
import struct
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
    
    #第一步：先拿报头
    header=cli.recv(4)
    #第二部：从报头中解析出对真实数据的描述信息
    total_size=struct.unpack('i',header)[0]
    #第二步：接收真实的数据
    recv_size=0
    recv_data=b''
    while recv_size<total_size:

        r_msg=cli.recv(1024)
        recv_data+=r_msg
        recv_size+=len(r_msg)

    print(len(recv_data))
    print(recv_data.decode('gbk'))

cli.close() 

