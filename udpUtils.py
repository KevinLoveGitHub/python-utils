#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import socket

root = Tk()
root.title("UDP 工具")
root.geometry("400x260")
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


def callback():
    address = (ip.get(), int(port.get()))
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = bytes(msg.get(), encoding="utf8")
    client.sendto(message, address)
    client.close()
    print(ip.get())
    print(port.get())
    print(msg.get())


f = Frame(root, height=100, width=80)
f.pack_propagate(0)
f.pack()

b = Button(f, text="发送", command=callback)
b.pack(fill=BOTH, expand=1)

ip_entry.focus()

root.mainloop()
