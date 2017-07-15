#!/usr/bin/env python
# encoding: utf-8

"""
@description: 运行爬虫

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: main.py
@time: 2016/12/23 20:40
"""

from scrapy import cmdline

def main():
    # cmdline.execute('scrapy crawl app_scrapy'.split())
    cmdline.execute('scrapy crawl ann9'.split())

if __name__ == '__main__':
    main()

