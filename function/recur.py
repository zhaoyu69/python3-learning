#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
#
# print(fact(5))

# def fact(n):
#     return fact_iter(n, 1)
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
#
# print(fact(5))

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)  # 直接把盘子从a移到c
    else:
        move(n - 1, a, c, b)  # 先把上面n-1个盘子，借助c，从a移到b
        move(1, a, b, c)  # 再把最下面的1个盘子，借助b，从a移到c
        move(n - 1, b, a, c)  # 最后把n-1个盘子，借助a，从b移到c

move(3,'A','B','C')