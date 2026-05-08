import socket
import subprocess
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
            #执行命令,并且拿到命令的结果
            result=subprocess.run(data,
                                  shell=True,
                                  capture_output=True,
                                  )
            if result.returncode==0:
                res=result.stdout
                print(len(res.decode('gbk')))
            else:
                res=result.stderr
                print(len(res.decode('gbk')))
            

            
            #返回结果
            con.send(res)
            
        except ConnectionResetError as e:
            print(e)
            break
    con.close()