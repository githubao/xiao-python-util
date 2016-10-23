# -*- coding: utf-8 -*-
__author__ = 'BaoQiang'

import os
import shutil
import os

"""
遍历文件夹，然后对文件操作
"""

def travel():
    root_path = "e:/movies/resources/movies/"

    for item in os.listdir(root_path):
        lists = item.split(".")[0].split(" ")
        if lists.__len__() != 3:
            print(item)
            continue

        print(lists[0].split("-")[0])


def re_name():
    root_path = "e:/movies/resources/test/"
    root_path = "e:/movies/resources/sample/movies/"
    root_path = "e:/movies/resources/sample/torrents/"
    root_path = "e:/movies/resources/torrents/"
    root_path = "e:/movies/resources/movies/"

    count = 1
    for item in os.listdir(root_path):
        shutil.move(root_path + item, root_path + str(count) + " " + item)
        print(count)

        count += 1

def gen_num():
    count = 1
    start = 1

    while count < 120:
        if count % 12 == 0:
            print("movies(%d-%d)解压密码：" % (start,count))
            start = count+1

        count+=1

if __name__ == "__main__":
    # travel()
    # re_name()
    gen_num()
