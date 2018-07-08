#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # 可变参数的求和
# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
#
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
# f=lazy_sum(*[1,3,5,7,9])
# print(f())

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print(f1(), f2(), f3()) # 9 9 9

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
#
# f1, f2, f3 = count()
# print(f1(), f2(), f3()) # 1 4 9

# def createCounter():
#     s = [0]
#     def counter():
#         s[0] = s[0] + 1
#         return s[0]
#     return counter

def createCounter():
    def x():
        n=1
        while True:
            yield n
            n=n+1
    it=x()
    def counter():
        return next(it)
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

