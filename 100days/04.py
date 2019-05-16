#!/usr/bin/python
# -*- coding: UTF-8 -*-

from math import sqrt

#输出乘法口诀表
for i in range(1,10):
    print
    for j in range(1, i+1):
        print "%d*%d=%d" % (i,j,i*j),

print "\n"
#判断是不是素数
num = 783930205
end = int(sqrt(num))
is_prime = True
for x in range(2, end+1):
    if num % x == 0:
        is_prime  = False
        break
if is_prime:
    print ('%d是素数' % num)
else:
    print('%d不是素数' % num)

