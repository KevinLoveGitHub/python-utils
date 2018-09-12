#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import os.path


def show_dir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        if '.git' not in item:
            print("|   " * depth + "+--" + item)

            new_item = path + '/' + item
            if os.path.isdir(new_item):
                show_dir(new_item, depth + 1)


if __name__ == '__main__':
    show_dir('/Users/Kevin/AndroidStudioProjects/Demo/Example/sourceset/src', 0)
