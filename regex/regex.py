#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的r前缀，就不用考虑转义的问题
# s = 'ABC\\-001'
# s1 = r'ABC\-001'
# print(s,s1)

# 匹配成功返回match对象，失败返回None
# import re
# m = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# print(m)
# m1 = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
# print(m1)
#
# test = '用户输入的字符串'
# if re.match(r'正则表达式', test):
#     print('ok')
# else:
#     print('failed')

# 切分字符串
# import re
# print('a b   c'.split(' '))
# print(re.split(r'\s+', 'a b   c'))
# print(re.split(r'[\s\,]+', 'a,b, c  d'))
# print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
#
# # 分组
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m)
# print(m.group(0)) # 原始字符串
# print(m.group(1)) # 1
# print(m.group(2)) # 2
#
# t = '19:05:30'
# m1 = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# print(m1.groups())
#
# # 贪婪匹配
# print(re.match(r'^(\d+)(0*)$', '102300').groups())
# # 非贪婪匹配
# print(re.match(r'^(\d+?)(0*)$', '102300').groups())
#
# # 编译
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# print(re_telephone.match('010-12345').groups())

# test
import re
def is_valid_email(addr):
    re_email = re.compile(r'^[0-9a-zA-Z\.]+@[a-z]+(.com)$')
    return re_email.match(addr)

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
    re_name = re.compile(r'<?([a-zA-Z\s]+)>?(\s?)(\w*)@(\w+)(.org)$')
    return re_name.match(addr).group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')