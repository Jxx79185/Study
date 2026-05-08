import socket
import subprocess#可以灵活操作命令结果的模块，用管道将命令结果重新定向
import struct
import json
ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.bind(('127.0.0.1',9900))
ser.listen(1)

while True:
    con,cli_addr=ser.accept()
    print(cli_addr)
    while True:
        try:
            #收命令
            data=con.recv(1024).decode('utf-8')
            print(f'对方发送信息：{data}')
            if data=='exit':
                print('对方准备断开链接')
                break
            #执行命令,并且拿到执行的结果
            result=subprocess.run(data,
                                  shell=True,
                                  capture_output=True,
                                  )

            res1=result.stdout
            res2=result.stderr
            #第一步：制作固定长度的报头的报头
            header_dic={'filename':"xxx.txt",
                        'md5':'xxdxxx',
                        'total_size':len(res1+res2)}      
            header_json=json.dumps(header_dic)
            header_bytes=header_json.encode('utf-8')
            header_h=struct.pack('i',len(header_bytes))#报头的报头
            con.send(header_h)    
            #第二步：把报头先发送给客户端
            con.send(header_bytes)
            #返回结果
            #第二步：再发真实的内容
            con.send(res1)
            con.send(res2)
            print(f'已发送字节长度为{len(res1+res2)}的文件')
            
        except ConnectionResetError as e:
            print(e)
            break
    con.close()