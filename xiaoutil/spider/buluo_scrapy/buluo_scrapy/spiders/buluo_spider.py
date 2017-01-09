# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from collections import namedtuple

Item = namedtuple('Item', ['title', 'followers', 'topics', 'describe'])


class BuluoSpiderSpider(scrapy.Spider):
    name = "buluo_spider"
    allowed_domains = ["buluo.qq.com"]
    start_urls = ['https://buluo.qq.com/p/category.html?cateid={}'.format(i) for i in range(10, 11)]

    def parse(self, response):
        items = []

        for item in response.xpath('//li[contains(@class,"collection-item")]'):
            title = item.xpath('.//a[contains(@class,"ellipsis")]/text()')[0].extract()
            followers = item.xpath('.//span[contains(@class,"pids")]/text()')[0].extract().replace('关注 ', '')
            topics = item.xpath('.//span[contains(@class,"fans")]/text()')[0].extract().replace('话题 ', '')
            describe = item.xpath('.//div[contains(@class,"desc")]/text()')[0].extract().strip().replace('\n', '')

            followers = form(followers)
            topics = form(topics)

            item = Item(title, followers, topics, describe)
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
