#!/usr/bin/python
# -*- coding: utf-8 -*-
from socket import *
import time

tcpSocket = socket(AF_INET, SOCK_STREAM)

# 重复使用绑定信息,不必等待2MSL时间
tcpSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

address = ('', 29900)
tcpSocket.bind(address)

tcpSocket.listen(5)

while True:
    time.sleep(0.01)
    print('开启等待')
    newData, newAddr = tcpSocket.accept()
    print('%s客户端已经连接，准备处理数据' % newAddr[0])
    try:
        while True:
            recvData = newData.recv(1024)
            if len(recvData) > 0:
                print(recvData)
            else:
                print('%s客户端已经关闭' % newAddr[0])
            break
    finally:
        newData.close()

tcpSocket.close()
