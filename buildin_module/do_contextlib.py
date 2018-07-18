#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 只要实现了上下文管理，都可以使用with语句
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
# class Query(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
# with Query('Bob') as q:
#     q.query()

# @contextmanager 让__enter__ __exit__变得简单
from contextlib import contextmanager
#
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
# # accept generator
# # 用yield语句把with ... as var把变量输出出去
# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')
#
# with create_query('Bob') as q:
#     q.query()

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

# 执行顺序
# 1. with语句首先执行yield之前的语句，因此打印出<h1>
# 2. yield调用会执行with语句内部的所有语句，因此打印出hello和world
# 3. 最后执行yield之后的语句，打印出</h1>。

# @closing 可以把没有上下文的对象变成上下文对象
# from contextlib import closing
# from urllib.request import urlopen
#
# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)

# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()