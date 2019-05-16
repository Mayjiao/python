#!/usr/bin/python
# -*- coding: UTF-8 -*-

from random import randint

face = randint(1,6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学猫叫'
elif face == 4:
    result = '念绕口令'
elif face == 5:
    result = '讲笑话'
else:
    result = '跑步'
print(result)
