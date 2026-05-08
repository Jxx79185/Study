
import socket
import time
cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cli.connect(("127.0.0.1",9900))

#时间较短，数据量较小的两个数据在进行发送时会因为Nagle算法被包装成一个数据进行发送，产生客户端这边的粘包
cli.send('hello'.encode('utf-8'))
time.sleep(1)
cli.send('world'.encode('utf-8'))
cli.send('dddddddddddddddddddddddd'.encode('utf-8'))