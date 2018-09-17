#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import socket

root = Tk()
root.title("UDP 工具")


def center_window(w, h):
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)


center_window(500, 500)


def encode_click(is_start: bool):
    print("encode_click", is_start)
    ip = "10.0.1.40"
    port = 1888
    if is_start:
        msg = "sonixcamerastart 30 1000 1 0"
    else:
        msg = "sonixcamerastop"

    print("encode_click", msg)
    address = (ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(bytes(msg, encoding="utf8"), address)
    client.close()


def decode_click(is_start: bool):
    print("decode_click", is_start)
    ip = "10.0.44.81"
    port = 1788
    if is_start:
        msg = "vdecplay 8 0 voplay:8:3:0:0:640:360:0:0:640:360 shine_net://@10.0.1.40:8899 " \
              "drawtext:80:128:128:128:128:0:0:128:128:128:empty:/mnt/fonts/simhei.ttf: ;"
    else:
        msg = "vdecstop 8 15 ;"

    print("decode_click", msg)
    address = (ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(bytes(msg, encoding="utf8"), address)
    client.close()


main_frame = Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

start_btn = Button(main_frame, text="开始编码", command=lambda: encode_click(True))
start_btn.pack(padx=10, pady=10)

stop_btn = Button(main_frame, text="停止编码", command=lambda: encode_click(False))
stop_btn.pack(padx=10, pady=10)

start_decode_btn = Button(main_frame, text="开始解码", command=lambda: decode_click(True))
start_decode_btn.pack(padx=10, pady=10)

stop_decode_btn = Button(main_frame, text="停止解码", command=lambda: decode_click(False))
stop_decode_btn.pack(padx=10, pady=10)
mainloop()
