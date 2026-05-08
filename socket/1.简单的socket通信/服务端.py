import socket

#1.买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建了一个套接字对象

#2.绑定手机卡
print(type(phone))
phone.bind(('127.0.0.1',8080))#绑定自己的ip以及端口（0-65535，0-1024是给操作系统使用的），127.0.0.1是本地回环地址，只监听本机的数据，一般用于测试

#3.开机
phone.listen(5)#开始监听,5代表在队列中最多可以有5个连接数等待，超出会在客户端显示连接错误

#等待电话链接
res=phone.accept()
connect,client_addr=res
print(f"收到 {client_addr} 的连接 | 新socket fd={connect.fileno()}")
data=connect.recv(1024)#表示最大收信长度为1024个字节，但是有个坑，目前不说
print(f'客户端的数据:{data}')
connect.send(data.upper())
connect.close()
phone.close()


