#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil

root_dir = '/Users/Kevin/AndroidStudioProjects'


def get_file_name(path):
    """ 删除所有项目下的 build 文件夹 """

    for root, dirs, files in os.walk(path, topdown=False):
        if root.endswith('/build'):
            shutil.rmtree(root)


if __name__ == '__main__':
    get_file_name(root_dir)
