#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#encode
print(u'中文测试正常')

#%格式化
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

#format
a='Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
print(a)

#test
s1=72
s2=85
r = (s2-s1)/s1*100
print('%.1f%%'%r)

