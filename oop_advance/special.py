#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
#     __repr__ = __str__
#
# print(Student('Michael'))
#
# s = Student('Michael')
# s

# 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值
#
# for n in Fib():
#     print(n)

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# print(Fib()[5])

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
#
# f = Fib()
# print(f[0])

# 但是list有个神奇的切片方法:
# Fib报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
# print(list(range(100))[5:10])

# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int): # n是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice): # n是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#
# f = Fib()
# print(f[0:5])
# print(f[:10])

# 要正确实现一个__getitem__()还有很多工作要做的...

# __getattr__

# class Student(object):
#
#     def __init__(self):
#         self.name = 'Michael'
#
# s = Student()
# print(s.name)
#
# # 当我们调用类的方法或属性时，如果不存在，就会报错。
# print(s.score)

# __getattr__()方法，动态返回一个属性

# class Student(object):
#
#     def __init__(self):
#         self.name = 'Michael'
#
#     def __getattr__(self, attr):
#         if attr=='score':
#             return 99
#
# s = Student()
# print(s.name)
# print(s.score)

# 利用完全动态的__getattr__，我们可以写出一个链式调用

# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
# print(Chain().status.user.timeline.list) # /status/user/timeline/list

# # try
# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         if path == 'users':
#             return lambda x: Chain('%s/%s/:%s' % (self._path, path, x))
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
# print(Chain().users('michael').repos) # /users/:user/repos

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，
# 判断一个变量是对象还是函数，需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

print(callable(Student('Michael')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

