# -*- coding: utf-8 -*-
import random
from collections import namedtuple

import scrapy
from scrapy.http import FormRequest
from scrapy.selector import Selector
import json

Item = namedtuple('Item', ['name', 'follow', 'topics', 'intro'])


class BuluoSpiderSpider(scrapy.Spider):
    name = "buluo_spider"
    allowed_domains = ["buluo.qq.com"]

    def __init__(self, bid):
        super(BuluoSpiderSpider, self).__init__()

        self.bid = bid
        self.start_urls = ['https://buluo.qq.com/p/category.html?cateid={}'.format(bid)]

    def start_requests(self):
        requests = []

        url = 'https://buluo.qq.com/cgi-bin/bar/get_bar_list_by_category'

        for i in range(10, 11):
            formdata = {
                'gflag': '1',
                'sflag': '0',
                'n': '3000',
                's': '0',
                'cateid': str(i),
                'r': str(random.random()),
                'bkn': ''
            }

            request = FormRequest(url, callback=self.parse_item, formdata=formdata)
            requests.append(request)

        return requests

    def parse_item(self, response):
        print('response code: {}'.format(response.status))

        items = []
        json_data = json.loads(response.text)
        category_name = ''

        for item in json_data['result']['bars']:
            name = item['name']
            follow = item['fans']
            topics = item['pids']
            intro = item['intro'].replace('\n', '')

            if not category_name:
                category_name = item['category_name']

            item = Item(name, follow, topics, intro)
            items.append(item)

        with open("C:\\Users\\BaoQiang\\Desktop\\res.txt", 'a') as fw:
            fw.write('{}\n'.format(category_name))

            for item in items:
                fw.write('{}\t{}\t{}\t{}\n'.format(item.name, item.follow, item.topics, item.intro))

            fw.write('{}\n'.format('*' * 50))

    def parse(self, response):
        items = []

        for item in response.selector.xpath('//li[contains(@class,"collection-item")]'):
            name = item.xpath('.//a[contains(@class,"ellipsis")]/text()')[0].extract()
            follow = item.xpath('.//span[contains(@class,"pids")]/text()')[0].extract().replace('关注 ', '')
            topics = item.xpath('.//span[contains(@class,"fans")]/text()')[0].extract().replace('话题 ', '')
            intro = item.xpath('.//div[contains(@class,"desc")]/text()')[0].extract().strip().replace('\n', '')

            follow = form(follow)
            topics = form(topics)

            item = Item(name, follow, topics, intro)
            items.append(item)

        with open("C:\\Users\\BaoQiang\\Desktop\\res.txt", 'w') as fw:
            for item in items:
                fw.write('{}\t{}\t{}\t{}\n'.format(item.title, item.followers, item.topics, item.describe))


def form(cnt):
    if '万' in cnt:
        res = float(cnt.replace('万', '')) * 10000
    else:
        res = cnt
    return int(res)


def test_xpath():
    html = open("C:\\Users\\BaoQiang\\Desktop\\10.html", 'r', encoding='utf-8').read()
    fw = open("C:\\Users\\BaoQiang\\Desktop\\res.txt", 'a')
    root = Selector(text=html)

    for item in root.xpath('//li[contains(@class,"collection-item")]'):
        title = item.xpath('.//a[contains(@class,"ellipsis")]/text()')[0].extract()
        followers = item.xpath('.//span[contains(@class,"pids")]/text()')[0].extract().replace('关注 ', '')
        topics = item.xpath('.//span[contains(@class,"fans")]/text()')[0].extract().replace('话题 ', '')
        describe = item.xpath('.//div[contains(@class,"desc")]/text()')[0].extract().strip().replace('\n', '')

        followers = form(followers)
        topics = form(topics)

        fw.write('{}\t{}\t{}\t{}\n'.format(title, followers, topics, describe))

    fw.close()


if __name__ == '__main__':
    test_xpath()
