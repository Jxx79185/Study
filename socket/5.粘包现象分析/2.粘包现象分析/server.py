import socket
import time 
ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.bind(('127.0.0.1',9900))
ser.listen(5)

con,cli_addr=ser.accept()
print(cli_addr)
res1=con.recv(1).decode('utf-8')
print(f'第一次的数据:{res1}')
# time.sleep(5)
res2=con.recv(1024).decode('utf-8')
print(f'第二次的数据:{res2}')
time.sleep(5)
res3=con.recv(10).decode('utf-8')
print(f'第三次的数据:{res3}')
res4=con.recv(10).decode('utf-8')
print(f'第三次的数据:{res4}')
#每次recv会把内存里面残留的的数据按能接收的字节尽量收取