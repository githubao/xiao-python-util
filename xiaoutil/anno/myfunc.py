#!/usr/bin/env python
# encoding: utf-8

"""
@description: as you see, my func

@author: BaoQiang
@time: 2017/6/4 19:10
"""

import os

root_path = 'F:/video/000'


def process():
    fw = open('C:\\Users\\BaoQiang\\Desktop\\1.txt', 'w', encoding='utf-8')

    for filename in os.listdir(root_path):
        if not filename.startswith('Common'):
        # if not filename.startswith('to'):
            continue

        sub_path = os.path.join(root_path, filename)
        for sub_filename in os.listdir(sub_path):
            full_name = os.path.join(sub_path, sub_filename)

            if os.path.isdir(full_name):
                continue

            # print(sub_filename)

            prefix, post = sub_filename.split('.')
            attrs = prefix.split(' ')

            fw.write('\t'.join(attrs))
            fw.write('\t{}'.format(filename))
            fw.write('\t{}'.format(len(attrs[2].split('(')[0])))
            fw.write('\n')

    fw.close()


def main():
    process()


if __name__ == '__main__':
    main()
