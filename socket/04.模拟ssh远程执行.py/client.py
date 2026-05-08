import socket
import time
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

    #拿命令的结果
    r_msg=cli.recv(600).decode('gbk')
    print(len(r_msg))
    print(r_msg)

cli.close() 