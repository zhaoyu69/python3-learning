#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map

# def f(x):
#     return x * x
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))
#
# L = []
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.append(f(n))
# print(L)
#
# print(list(map(str,[1,2,3,4,5,6,7,8,9])))

# reduce

# from functools import reduce
# def add(x,y):
#     return x + y
#
# print(reduce(add, [1,3,5,7,9]))
#
# def fn(x,y):
#     return x * 10 + y
#
# print(reduce(fn, [1,3,5,7,9]))
#
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def char2num(s):
#     return DIGITS[s]
#
# def str2int(s):
#     return reduce(lambda x, y : x * 10 + y, map(char2num, s))
#
# print(str2int('12345'))

# test1

def normalize(name):
    return name[:1].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# test2

def prod(L):
    def cj(x, y):
        return x * y
    return reduce(cj, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# test3

def str2float(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    s1, s2 = s.split('.')
    d1 = reduce(lambda x, y: x * 10 + y, map(lambda x: digits[x], s1))
    d2 = reduce(lambda x, y: x * 0.1 + y, map(lambda x: digits[x], reversed(s2))) * 0.1
    return d1 + d2

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')