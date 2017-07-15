# -*- coding: utf-8 -*-
__author__ = 'BaoQiang'

import requests
from bs4 import BeautifulSoup
import win_inet_pton
# import socket
import os
import re
import time

"""
爬取路透社网站的新闻数据
"""

root_url = "http://uk.reuters.com/"
start_url = "http://uk.reuters.com/news/archive/oilRpt?view=page&page=%d&pageSize=10"

root_out_path = "C:\\Users\\BaoQiang\\Desktop\\news\\"

url_file = root_out_path+"news_url.txt"

f_article = open(root_out_path+"article_urls.txt", "a")
f_err = open(root_out_path+"news_err.txt", "a")

proxies = {
    "http": "socks5://127.0.0.1:1080",
    "https": "socks5://127.0.0.1:1080",
}


def get_all_url():
    f_out = open(url_file, "w")

    for i in range(1, 2801):
        url = start_url % i

        try:
            html_data = requests.get(url, proxies=proxies)

            soup = BeautifulSoup(html_data.text, "lxml")

            title = soup.select(".story-title a")

            for item in title:
                f_out.write(root_url + item["href"] + "\n")
        except Exception as e:
            print(url)
            print(e)

        if i % 10 == 0:
            print("process..." + str(i))

    f_out.close()


def get_content():
    f_in = open(url_file, "r")
    urls = f_in.readlines()

    i = 0
    for url in urls:
        url = url.replace("\n", "")

        time_tuple = ""
        title = ""

        try:
            html_data = requests.get(url, proxies=proxies)

            if html_data.status_code == 200:
                soup = BeautifulSoup(html_data.text, "lxml")

                titles = soup.select(".article-headline")
                for item in titles:
                    title = item.text

                time_stamp = soup.select(".timestamp")
                for item in time_stamp:
                    time_tuple = trans_time(item.text)

                file_name = get_file_name(title, time_tuple,url)
                f_out = open(file_name, "w")

                article_text = soup.select("#articleText p")
                for item in article_text:
                    content = item.text.strip().replace("\n", " ").replace("\t", " ")
                    f_out.write(content.encode("utf-8") + "\n")

                f_out.close()

            else:
                print(html_data.status_code)
                f_err.write(html_data.status_code + "\n")
                f_err.write(url + "\n")

        except Exception as e:
            print(e)
            f_err.write(str(e) + "\n")
            f_err.write(url + "\n")

        i += 1

        # if i == 3:
        #     break

        if i % 10 == 0:
            print("process..." + str(i))

    f_in.close()
    f_err.close()
    f_article.close()

# 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
def trans_time(str):
    old_str = str

    str = str.replace(" BST", "")
    str = str.replace(" GMT", "")

    try:
        time_stamp = time.mktime(time.strptime(str, "%a %b %d, %Y %H:%M%p"))
        time_array = time.localtime(time_stamp)
        # format_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        year = time.strftime("%Y", time_array)
        month = time.strftime("%m", time_array)
        day = time.strftime("%d", time_array)

        time_tuple = (year, month, day)
        # print time_tuple

        return time_array


    except Exception as e:
        print(e)
        print(old_str)
        return None


def escape_chars(title):
    # es_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '\'']
    # new_title = ""
    #
    # for item in es_chars:
    #     new_title = title.replace(item, "")
    #
    # return new_title
    # 只剩下英文和空格
    p = re.compile('[^\w\s-]')
    new_title = p.sub("", title)
    return new_title

#根据title的文件名，顺便保存文章的url
def get_file_name(title, time_tuple, url):
    new_title = escape_chars(title)
    f_article.write(new_title+"\n"+url+"\n")
    f_article.write("-"*100+"\n")

    year = time_tuple[0]
    month = time_tuple[1]
    day = time_tuple[2]

    file_path = "%s%d/%d/%d" % (root_out_path, year, month, day)

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_name = file_path + "/" + str(new_title) + ".txt"

    return file_name


def test():
    # a = "Sat Mar 28 22:24:24 2016"
    # print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

    # a = "Thu Oct 16, 2014 9:50pm"
    # print time.mktime(time.strptime(a, "%a %b %d, %Y %H:%M%p"))

    # s = 'Authorities shut Istanbul\'s Bosphorus to tankers for "security reasons" - agent'
    # # print re.sub("[^a-zA-Z -]","", s)
    # print re.sub("[^\w\s-]", "", s)

    pass

def process_err():
    f = open(root_out_path+"news_err.txt","r")
    f_out = open(root_out_path+"fail_urls.txt","w")
    lines = f.readlines()
    for line in lines:
        if line.find("reuters")>-1:
            f_out.write(line)

    f.close()
    f_out.close()


def count_sum(dirname,filter_types=[]):
     '''Count the files in a directory includes its subfolder's files
        You can set the filter types to count specific types of file'''
     count=0
     filter_is_on=False
     if filter_types!=[]: filter_is_on=True
     for item in os.listdir(dirname):
         abs_item=os.path.join(dirname,item)
         #print item
         if os.path.isdir(abs_item):
             #Iteration for dir
             count+=count_sum(abs_item,filter_types)
         elif os.path.isfile(abs_item):
             if filter_is_on:
                 #Get file's extension name
                 extname=os.path.splitext(abs_item)[1]
                 if extname in filter_types:
                     count+=1
             else:
                 count+=1

     return count

if __name__ == "__main__":
    print("start_time: %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    # get_all_url()
    # get_content()
    # process_err()
    print(count_sum(root_out_path))
    # test()


    print("end_time: %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
