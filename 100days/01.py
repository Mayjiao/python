#!/usr/bin/python
# -*- coding: UTF-8 -*-

print('hello world!')
#此处末尾加逗号是为了不换行
print 'goodbye world!',
print('你好,世界')
print '告别,世界'

pi = 3.141592653
print('%10.3f' % pi)
print('%-10.3f' % pi)
print('%+10.3f' % pi)
print('%.1f' % pi)

print('%s' % 'hello world')

print('{} {}'.format('hello','world'))
print('{0} {1}'.format('hello','world'))
print('{0} {1} {0}'.format('hello','world'))
print('{1} {1} {0}'.format('hello','world'))
