#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# itertools 用于操作迭代对象的函数
import itertools
# count() 无限自然数序列
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cycle() 无限重复传入序列
# cs = itertools.cycle('ABC') # 字符串也是序列的一种
# for c in cs:
#     print(c)

# repeat() 次数重复传入序列
# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))

# chain() 串联一组迭代对象
# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# groupby() 把迭代器中相邻的重复元素挑出来放在一起
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))
#
# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
#     print(key, list(group))

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odds = itertools.count(start=1, step=2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    os = itertools.takewhile(lambda x: (x + 1) / 2 <= N, odds)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    L = list(map(lambda x: (-1 if ((x + 1) / 2) % 2 == 0 else 1) * 4 / x, list(os)))
    # step 4: 求和:
    return sum(L)

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')