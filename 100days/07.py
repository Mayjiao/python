#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time

#yield关键字将一个普通函数改造成生成器函数
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b=b,a+b
        yield a

def main():
    for val in fib(20):
        print val

if __name__ == '__main__':
    main()

#显示跑马灯文字
def pao():
    content = '北京欢迎你为你开天辟地'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:]+content[0]

pao()

