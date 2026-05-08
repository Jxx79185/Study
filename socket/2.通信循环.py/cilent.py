import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))
print('连接成功')
while True:
    msg=input('>>').strip()
    if not msg:
        continue
    phone.send(msg.encode('utf-8'))
    if msg=='exit':
        print('告诉对方我要准备挂电话了')
        break
    data=phone.recv(1024).decode('utf-8')
    print(data)   
phone.close()
    

