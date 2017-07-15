# -*- coding: utf-8 -*-
import traceback
import re

import scrapy
from scrapy.http.request import Request
from scrapy.selector import Selector


class Ann9Spider(scrapy.Spider):
    name = "ann9"
    allowed_domains = ["http://www.ann9.com"]
    start_urls = ['http://www.ann9.com/33_11?p=0&n=1']

    cookies = {
        "udata": "6cb04fea1a6d4217991f4464bcad89ff",
        "CNZZDATA4284205": "cnzz_eid%3D97100975-1482481349-%26ntime%3D1482492188",
    }

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies=self.cookies)

    def parse(self, response):
        with open('C:\\Users\\BaoQiang\\Desktop\\spider.txt', 'w', encoding='utf-8') as f:
            containers = response.selector.xpath('//div[contains(%class,"padtit1xia1")]')
            for c in containers:
                f.write(c.text)


def test_xpath():
    html = open("C:\\Users\\BaoQiang\\Desktop\\ann9.html", 'r', encoding='utf-8').read()
    root = Selector(text=html).xpath('//div[contains(@class,"padtit1xia1")]')
    fw = open("C:\\Users\\BaoQiang\\Desktop\\app_res.txt", 'w', encoding='utf-8')

    cnt = 0
    for contain in root.xpath('div'):
        try:
            describe = contain.xpath('span').xpath('a')[0].xpath('@title').extract()[0]
            if '-' in describe or '—' in describe:
                describes = re.split('[—-]+', describe)
                describes = [item.strip() for item in describes]
                title, *items = describes
                content = '-'.join(items)
            else:
                title = describe.strip()
                content = 'none'

            title = re.sub('（.*）|\(.*\)','',title)

            classes = contain.xpath('span[contains(@class,"padlan1")]')[1].xpath('text()').extract()[1]

            cnt += 1
            fw.write('{}\t{}\t{}\t{}\n'.format(cnt, title, content, classes))

        except Exception as e:
            cnt += 1
            fw.write('error{}\t{}\t{}\t{}\n'.format(cnt, title, content, classes))
            traceback.print_exc()

    fw.close()


def test():
    describe = '芒果TV—直播2017年湖南卫视跨年演唱会'
    describes = re.split('[—-]+', describe)
    print(describes)

if __name__ == '__main__':
    test_xpath()
    # test()
