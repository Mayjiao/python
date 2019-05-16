#!/usr/bin/python
# -*- coding: UTF-8 -*-

#判断是否是回文数
def is_huiwen(num):
    temp = num
    total = 0
    while temp > 0:
        total = total *10 + temp%10
        temp //= 10
    return total == num

is_huiwen(12321)
