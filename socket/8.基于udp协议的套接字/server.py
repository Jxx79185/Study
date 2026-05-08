from socket import socket,AF_INET,SOCK_DGRAM

server=socket(AF_INET,SOCK_DGRAM)

server.bind(('127.0.0.1',8080))

