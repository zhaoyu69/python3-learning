#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式
print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0 ])

print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出文件和目录
import os
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if isinstance(i, str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')