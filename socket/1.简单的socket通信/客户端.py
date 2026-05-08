import socket
#1.买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2.拨号（客户端不用进行绑定ip）
phone.connect(('127.0.0.1',8080))
#3.发，收消息
HEADER_TEXT = b'TXT|'
msg=input('>>')
phone.send(HEADER_TEXT+msg.encode('utf-8'))
data=phone.recv(1024)
print(data)
phone.close()