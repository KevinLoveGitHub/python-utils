#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil

root_dir = '/Users/Kevin/Workspaces/Shine/人脸识别/lfw'

def getFileName(path):
    ''' 获取指定目录下的所有指定后缀的文件名 '''

    f_list = os.listdir(path)
    # print f_list
    for index,i in enumerate(f_list):
        if index == 1001:
            return
        i = path + '/' +i
        is_dir = os.path.isdir(i)
        if is_dir:
            image_list = os.listdir(i)
            for num, image in enumerate(image_list):
                if os.path.splitext(image)[1] == '.jpg' and num == 0:
                    if not os.path.exists(root_dir + '/image/' + image):
                        print(image)
                        shutil.copy2(i + '/' + image, root_dir + '/image')
            # os.path.splitext():分离文件名与扩展名





if __name__ == '__main__':
    path = root_dir
    getFileName(path)
