#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lambda 匿名函数

f = lambda x: x * x
print(f(5))

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

_L = list(filter(lambda x : x % 2 == 1, range(1, 20)))
print(_L)

