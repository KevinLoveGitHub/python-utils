#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom import minidom
import os


def alter(file, old_str, new_str, file_name):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param file_name: 新文件名
    :param file: 文件路径
    :param old_str: 需要替换的字符串
    :param new_str: 替换的字符串
    :return: None
    """
    with open(file, "r", encoding="utf-8") as f1, open("%s.svg" % file_name, "w", encoding="utf-8") as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str, new_str)
            f2.write(line)


doc = minidom.parse("/Users/Kevin/Downloads/iconfont/iconfont.svg")  # parseString also exists

for path in doc.getElementsByTagName('glyph'):
    print(path.getAttribute('d'))
    print(path.getAttribute('glyph-name'))
    old = 'M508.8 851.2c-256 0-464-208-464-464s208-464 464-464 464 208 464 464S764.8 851.2 508.8 851.2zM508.8-28.799999999999955c-230.4 0-416 185.6-416 416s185.6 416 416 416 416-185.6 416-416S739.2-28.799999999999955 508.8-28.799999999999955zM521.6 243.20000000000005c12.8 0 22.4 9.6 22.4 22.4l0 428.8c0 12.8-9.6 22.4-22.4 22.4-12.8 0-22.4-9.6-22.4-22.4l0-428.8C496 256 508.8 243.20000000000005 521.6 243.20000000000005zM521.6 147.20000000000005m-35.2 0a1.1 1.1 0 1 1 70.4 0 1.1 1.1 0 1 1-70.4 0Z'
    alter('/Users/Kevin/Downloads/all.svg', old, path.getAttribute('d'), path.getAttribute('glyph-name'))

doc.unlink()
