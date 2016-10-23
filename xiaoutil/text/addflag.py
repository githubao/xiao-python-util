# -*- coding: utf-8 -*-
__author__ = 'BaoQiang'

import os

"""
给文件末尾，加特殊字符，以修改文件的MD5
"""

def add_flag():
    # root_path = "e:/movies/resources/movies/"
    root_path = "d:/dls/"
    out_path = "d:/outs/"

    count = 1
    for item in os.listdir(root_path):
        os.system("d:")
        os.system(root_path)
        cmd = "copy \"%s\" /b + \"%s\" /a \"%s\"" % ((item, out_path + "0.txt", out_path + item))
        print(cmd)
        os.system(cmd)

        print(count)
        count += 1


if __name__ == "__main__":
    add_flag()
