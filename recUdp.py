#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from tkinter import *
import socket

root = Tk()
root.title("UDP 工具")
root.geometry("400x300")
root.resizable(width=False, height=False)

ip_label = Label(root, text="输入 IP 地址：")
ip_label.pack()

ip = StringVar()
ip_entry = Entry(root, textvariable=ip)
ip_entry.pack()

port_label = Label(root, text="输入端口：")
port_label.pack()

port = StringVar()
port_entry = Entry(root, textvariable=port)
port_entry.pack()

msg_label = Label(root, text="输入需要发送消息：")
msg_label.pack()

msg = StringVar()
msg_entry = Entry(root, textvariable=msg)
msg_entry.pack()

#
# f = Frame(root, height=100, width=80)
# f.pack_propagate(0)
# f.pack()

btn1 = Button(root, text="发送", command=lambda: callback(1), compound=CENTER)
btn1.pack()

msg_label2 = Label(root, text="输入需要发送消息：")
msg_label2.pack()
msg2 = StringVar()
msg_entry2 = Entry(root, textvariable=msg2)
msg_entry2.pack()
btn2 = Button(root, text="发送", command=lambda: callback(2), compound=CENTER)
btn2.pack()


def callback(index):
    address = (ip.get(), int(port.get()))
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_msg = msg.get() if index == 1 else msg2.get()
    message = bytes(send_msg, encoding="utf8")
    client.sendto(message, address)
    client.close()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(ip.get(), port.get(), send_msg)


ip_entry.focus()

root.mainloop()
