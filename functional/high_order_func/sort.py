#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(sorted([36, 5, -12, 9, -21]))

# key指定按照绝对值的方式排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 对字符串排序，是按照ASCII的大小比较的
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# test
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

def by_score(t):
    return -t[1]


L1 = sorted(L, key=by_name)
print(L1)

L2 = sorted(L, key=by_score)
print(L2)