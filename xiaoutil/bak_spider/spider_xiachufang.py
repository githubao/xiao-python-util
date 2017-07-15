# -*- coding: utf-8 -*-
__author__ = 'BaoQiang'

import requests
from bs4 import *
from time import *

"""
爬取下厨房全网数据
"""

xiachufang_url = "https://www.xiachufang.com"


def spider_all_recipe():
    base_url = "http://www.xiachufang.com/recipe/"

    # f = open("C:\\Users\\BaoQiang\\Desktop\\recipe.txt", "w")
    f_out = open("/mnt/baoqiang/recipe.txt", "w")
    f_in = open("/mnt/baoqiang/recipe_in.txt", "r")
    urls = f_in.readlines()

    proxies = {
        "http": "http://127.0.0.1:10800",
        "https": "http://127.0.0.1:10800",
    }

    count = 0
    for url in urls:
        url = url.replace("\n", "")
        try:
            # http_response = requests.get(url,proxies=proxies)
            http_response = requests.get(url)
            if http_response.status_code == 200:
                soup = BeautifulSoup(http_response.text, "lxml")

                title = soup.select("h1")[0].get_text().encode("utf-8").strip()
                number = soup.select(".cooked .number")[0].get_text().encode("utf-8").strip()

                # print(title)
                f_out.write(title + "\t" + number + "\t" + url.encode("utf-8") + "\n")
                # print(title + "\t" + number + "\n")

                # sleep(2)

            else:
                print(http_response.status_code)
                print(url)
                print(asctime(localtime(time())))
                # sleep(2)

        except Exception as e:
            print(url + "\t")
            print(e)
            print("\n")

        count += 1
        print(count)

    f_out.close()


def get_cate_urls(start_url):
    cate_urls = []
    http_response = requests.get(start_url)
    if http_response.status_code == 200:
        soup = BeautifulSoup(http_response.text, "lxml")

        cates_open = soup.select(".level2.plain.list a")

        for item in cates_open:
            # print item["href"]
            cate_urls.append(xiachufang_url + item["href"])

        return cate_urls


def spider_category():
    start_url = "https://www.xiachufang.com/category/40076/"

    f = open("C:\\Users\\BaoQiang\\Desktop\\recipe.txt", "w")
    # f = open("/mnt/baoqiang/recipe.txt", "w")

    cate_url_list = get_cate_urls(start_url)

    if cate_url_list is None:
        return None

    count = 0
    for cate_url in cate_url_list:

        for i in range(1, 1000):
            new_url = cate_url + "?page=%s" % i

            try:
                http_response = requests.get(new_url)
                if http_response.status_code == 200:
                    soup = BeautifulSoup(http_response.text, "lxml")

                    recipe_urls = soup.select(".normal-recipe-list a")

                    for recipe_url in recipe_urls:
                        print(recipe_url["href"])
                        f.write(xiachufang_url + recipe_url["href"] + "\n")

                        count += 1
                        print(count)

                else:
                    break


            except Exception as e:
                print(str(new_url) + "\t")
                print(e)
                print("\n")

    f.close()


if __name__ == "__main__":
    spider_all_recipe()

    # get_cate_urls("https://www.xiachufang.com/category/40076/")
    # spider_category()

    print("end")
    print(asctime(localtime(time())))
