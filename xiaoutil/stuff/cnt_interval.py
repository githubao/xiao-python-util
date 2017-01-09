#!/usr/bin/env python
# encoding: utf-8

"""
@description: 区间统计

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: cnt_interval.py
@time: 2016/12/21 10:57
"""

from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt


def interval(j):
    f = open('C:\\Users\\BaoQiang\\Desktop\\plt\\num{}.txt'.format(j), 'r', encoding='utf-8')
    lines = f.readlines()
    nums = [int(float(line.strip()) * 100) for line in lines]

    d = {}
    for i in range(0, 10):
        d[i * 10] = 0

    for num in nums:
        for i in range(0, 10):
            if i * 10 <= num < (i + 1) * 10:
                d[i * 10] += 1
                break
            if num == 100:
                d[90] += 1
                break

    l = sorted(d.items(), key=itemgetter(0))

    cnt = sum(item[1] for item in l)

    l = [(item[0], float('{0:.5f}'.format(item[1] / cnt))) for item in l]

    f = open('C:\\Users\\BaoQiang\\Desktop\\plt\\distribute{}.txt'.format(j), 'a', encoding='utf-8')

    # f.write('{} {}\n'.format(j, '*' * 50))
    for item in l:
        k, v = item
        f.write('[{}-{}] {}\n'.format(k, k + 10, float('{0:.5f}'.format(v * 100))))

    f.close()

    draw(l, j)


def draw(l, j):
    fig = plt.figure(j)

    bar_width = 0.35
    idx = range(len(l))
    v = [item[1] for item in l]
    rect = plt.bar(idx, np.array(v), bar_width, color='#0072BC', label='hhh')

    plt.xlabel("分值区间",fontproperties='SimHei')
    plt.ylabel("百分占比",fontproperties='SimHei')

    # plt.text(rect.get_x(), rect.get_width() / 2, rect.get_height(), rect.get_height(), ha='center', va='bottom')
    # plt.show()
    plt.savefig('C:\\Users\\BaoQiang\\Desktop\\plt\\figure{}.png'.format(j))
    plt.close(j)


def main():
    for j in range(0, 4):
        interval(j + 1)


if __name__ == '__main__':
    main()
