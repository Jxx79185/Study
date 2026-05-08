import socket
cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cli.connect(("127.0.0.1",8080))
while True:
    s_msg=input('>>')
    if not s_msg:
        continue
    cli.send(s_msg.encode('utf-8'))
    if s_msg=='exit':
        print('准备断开连接')
        break
    r_msg=cli.recv(1024).decode('utf-8')
    print(r_msg)

cli.close() 