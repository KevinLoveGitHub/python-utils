#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import socket

HOST = '127.0.0.1'
PORT = 29900
BUFSIZE = 1024
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

while True:
    print('wating for message...')
    data, addr = server.recvfrom(BUFSIZE)
    reply = 'Hello, %s!' % data.decode('utf-8')
    server.sendto(reply.encode('utf-8'), addr)
