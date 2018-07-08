#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def now():
#     return '2018-07-08'
#
# f=now
# print(f())
# print(f.__name__)

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2018-07-08')
#
# now()

# 给decorator本身传入参数
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2018-07-08')
#
# now()

# wrapper.__name__ = func.__name__
# import functools
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# test1
# import time, functools
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         before = time.time()
#         r = fn(*args, **kw)
#         consumed = (time.time() - before) * 1000
#         print("执行%s耗时：%f ms" % (fn.__name__, consumed))
#         return r
#     return wrapper
#
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

# test2

import functools
def log(text=''):
    def decorator(text, func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
