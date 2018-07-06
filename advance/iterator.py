#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 可作用于for循环的list,tuple,set,str,生成器generator是迭代对象。
# 生成器generator是迭代器,而其他不是
# 将他们变成迭代器 iter()

from collections import Iterator
print(isinstance(iter([]), Iterator))

for x in [1, 2, 3, 4, 5]:
    pass

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        print('StopIteration')
        break