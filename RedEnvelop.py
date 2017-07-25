#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
# 微信红包程序

import random
from concurrent.futures import ThreadPoolExecutor
import time

# 领红包的主要程序
def distribute(number, money):
    # 判断人数是不是整数
    if type(number) == type(1):
        moneymin = 0.01
        # 最大的数为平均数的2倍
        moneymax = money / number * 2
        # 判断钱是不是小于人头总数
        if money > number * 0.01:
            getmoney = random.randint(1, 100) / 100 * moneymax
            if getmoney < moneymin:
                getmoney = moneymin
                return round(getmoney, 2)
            else:
                return round(getmoney, 2)
        elif money == number * 0.01:
            return 0.01
        else:
            print("钱少于人头数，请重新输入...")
            exit()

    else:
        print("输入的不是整数，请重新输入...")
        exit()


# 多线程领红包
def getthread(number, money):
    a = []
    # 进程数
    pool = ThreadPoolExecutor(int(number))
    temp = number
    for i in range(number):
        if i + 1 == temp:
            getmoney = money
            print("第" + str(i + 1) + "个人得到了" + str(getmoney) + "元钱，红包已经被领完！")
        else:
            result = pool.submit(distribute, number, money)
            getmoney = result.result()
            number = number - 1
            money = round(money - getmoney, 2)
            print("第" + str(i + 1) + "个人得到了" + str(getmoney) + "元钱，还剩下" + str(number) + "个红包没有人领取，还剩下" + str(
                money) + "元钱！")

        a.append(getmoney)
    return a


if __name__ == '__main__':
    number = int(input("发送红包个数："))
    money = float(input("发送红包金额："))

    # number = 500
    # money = 200

    # 程序测速
    a = time.clock()
    arr = []
    # arr.append(distribute(number, money))
    arr = getthread(number, money)
    sum = 0
    for item in arr:
        sum = sum + item
    # 程序测速
    b = time.clock()

    print("总共发送的钱为" + str(round(sum, 2)) + " 程序运行时间为：" + str(b - a))