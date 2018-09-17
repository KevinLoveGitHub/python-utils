#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time


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


def timer(seconds):
    while True:
        encode_click(False)
        decode_click(False)

        time.sleep(5)

        encode_click(True)
        decode_click(True)

        time.sleep(seconds)


if __name__ == '__main__':
    timer(60 * 60)
