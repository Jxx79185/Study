import socket

ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.bind(('127.0.0.1',8080))
ser.listen(1)

while True:
    con,cli_addr=ser.accept()
    print(cli_addr)
    while True:
        try:
            data=con.recv(1024).decode('utf-8')
            print(f'对方发送信息：{data}')
            if data=='exit':
                print('对方准备断开链接')
                break

            con.send(data.upper().encode('utf-8'))
            
        except ConnectionResetError as e:
            print(e)
            break
    con.close()

ser.close()
