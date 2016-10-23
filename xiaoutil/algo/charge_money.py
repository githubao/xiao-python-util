# -*- coding: utf-8 -*-
__author__ = 'BaoQiang'

#!/usr/bin/env python
#coding:utf-8

"""
给定无限硬币，给定固定金额的钱，找出数量最少的硬币组合
"""

def change_coin(money):
    coin = [1,2,5,10,20,50,100]     #1分，2分，5分，1角，2角，5角，1元
    # coin = [1,5,10,21,25]     #1分，2分，5分，1角，2角，5角，1元
    coin.sort(reverse=True)
    money = money*100               #以分为单位进行计算
    change = {}

    for one in coin:
        num_coin = money//one       #除法，取整，得到该单位硬币的个数
        if num_coin>0:
            change[one]=num_coin
        num_remain = money%one      #取余数，得到剩下的钱数
        if num_remain==0:
            break
        else:
            money = num_remain
    return change

if __name__=="__main__":
    money = 1.23
    # money = 3.42
    num_coin = change_coin(money)
    result = [(key,num_coin[key]) for key in sorted(num_coin.keys())]
    print("You have %s RMB" % money)
    print("I had to change you:")
    print("    Coin    Number")
    for i in result:
        # if i[0]==100:
        #     print "Yuan    %d    %d"%(i[0]/100,i[1])
        # elif i[0]<10:
        #     print "Fen    %d    %d"%(i[0],i[1])
        # else:
        #     print "Jiao    %d    %d"%(i[0]/10,i[1])
        print("Jiao    %d    %d" % (i[0], i[1]))
