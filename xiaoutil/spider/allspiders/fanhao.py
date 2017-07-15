#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/15 11:41
"""

import scrapy
from scrapy import cmdline

out_file = 'C:\\Users\\BaoQiang\\Desktop\\1.txt'

class FanhaoSpider(scrapy.Spider):
    name = 'fanhao_spider'

    start_urls = []
    start_urls = ['http://www.fanhao123.org/L/nvyou{}.html'.format(i) for i in range(2, 27)]
    start_urls.append('http://www.fanhao123.org/L/nvyou.html')


    def parse(self, response):
        classes = response.selector.xpath('//ul/li/p/a/text()')
        for item in classes:
            with open(out_file,'a',encoding='utf-8') as fw:
                fw.write('{}\t{}\n'.format(response.url,item.extract().strip().split('(')[0]))


def main():
    cmdline.execute('scrapy crawl fanhao_spider'.split())


if __name__ == '__main__':
    main()
