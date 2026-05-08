import socket
import time
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8080))
phone.listen(5)
con,client_addr=phone.accept()
print(client_addr)
while True:#通信循环
    try:
        data=con.recv(1024)
        msg=data.decode('utf-8')
        print(msg)
    except ConnectionResetError as e:
        print(e)
        break
    time.sleep(1)
    if msg=='exit':
        print('对方准备挂断电话')
        break
    con.send(data.upper())
con.close()
phone.close()

