#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[:3])
# print(L[-2:-1])

L = list(range(100))
print(L)

# 前十个数 每两个取一个
print(L[:10:2])

# 所有数 每五个取一个
print(L[::5])

# tuple 切片
print((0, 1, 2, 3, 4, 5)[:3])

# str 切片
print('ABCDEFG'[:3])

def trim(s):
    if s[:1] == " ":
        return trim(s[1:])
    elif s[-1:] == " ":
        return trim(s[:-2])
    else:
        return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
