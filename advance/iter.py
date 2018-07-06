#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# d = {'a': 1, 'b': 2, 'c': 3}
# d = 'ABC'
# for key in d:
#     print(key)

# 判断是否为可迭代对象
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

# 索引迭代
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
        return (min, max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')




