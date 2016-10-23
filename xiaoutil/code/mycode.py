# -*- coding: utf-8 -*-
__author__ = 'BaoQiang'


def my_decode():
    f_in = open("C:\\Users\\BaoQiang\\Desktop\\out.txt", "r")
    fw = open("C:\\Users\\BaoQiang\\Desktop\\out2.txt", "w")

    data = f_in.read().decode("unicode_escape")

    fw.write(data.encode("utf-8"))


if __name__ == "__main__":
    my_decode()
