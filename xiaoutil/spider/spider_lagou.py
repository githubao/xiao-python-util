# -*- coding: utf-8 -*-
__author__ = 'BaoQiang'

import requests
from bs4 import BeautifulSoup
import json

"""
爬取拉勾全网数据
"""

f_in = open("C:\\Users\\BaoQiang\\Desktop\\company.txt", "r")
f_out = open("C:\\Users\\BaoQiang\\Desktop\\company_info.txt", "w")
lagou = "http://www.lagou.com/gongsi/"


def spider_all_company():
    f_out = open("C:\\Users\\BaoQiang\\Desktop\\company.txt", "w")

    count = 0
    for i in range(1, 720):
        url = "http://www.lagou.com/gongsi/2-0-0.json?first=false&pn=%s&sortField=0&havemark=0" % i

        http_response =requests.post(url)
        try:
            if http_response.status_code == 200:
                response_data = http_response.text
                response_dict = eval(str(response_data.encode("utf-8")))
                results = response_dict["result"]

                for item in results:
                    company_id = item["companyId"]
                    company_url = lagou + "%s.html" % company_id
                    f_out.write(company_url + "\n")
            else:
                print(http_response.status_code)
        except Exception as e:
            print(url)
            print(e)

        count += 1
        print(count)

        # if count == 3:
        # break


def spider_company_info():
    urls = f_in.readlines()

    count = 0
    for url in urls:
        url = url.replace("\n", "")
        try:
            http_response = requests.get(url)

            if http_response.status_code == 200:
                soup = BeautifulSoup(http_response.text, "lxml")
                company_basic_info = soup.select("#basic_container span")

                for item in company_basic_info:
                    f_out.write(item.get_text().encode("utf-8").replace("\n", "").strip().replace("\t", "") + "\t")

                f_out.write(url+"\t")

                company_product = soup.select(".product_details .product_profile")
                for item in company_product:
                    f_out.write(item.get_text().encode("utf-8").replace("\n", "").strip().replace("\t", "") + "\t")

                company_info = soup.select(".company_content")
                for item in company_info:
                    f_out.write(item.get_text().encode("utf-8").replace("\n", "").strip().replace("\t", "") + "\t")

                company_location = soup.select(".mlist_li_desc")
                number = 0
                for item in company_location:
                    if company_location.__len__() != (number + 1):
                        f_out.write(item.get_text().encode("utf-8").replace("\n", "").strip().replace("\t", "") + "|")
                    else:
                        f_out.write(item.get_text().encode("utf-8").replace("\n", "").strip().replace("\t", ""))

                    number += 1

                f_out.write("\n")

            else:
                print(http_response.status_code)

            count += 1
            print(count)

            # if count == 3:
            #     break

        except Exception as e:
            print(url)
            print(e)


if __name__ == "__main__":
    # spider_all_company()
    spider_company_info()
