#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TCP
import socket

# Client
# # create
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # connect
# s.connect(('www.sina.com.cn', 80))
#
# # AF_INET IPV4
# # AF_INET6 IPV6
# # SOCK_STREAM 使用面向流的TCP协议
# # connect 参数是tuple 包含ip和port
#
# # send
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# # receive
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
#
# # close
# s.close()
#
# # handle data to file
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# with open('sina.html', 'wb') as f:
#     f.write(html)

# Server
# create
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
s.bind(('127.0.0.1', 9999))

# listen
s.listen(5)
print('Waiting for connection...')

# accept
import threading, time
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
