#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# print(power(5))

# def add_end(L=[]):
#     L.append('END')
#     return L
#
# print(add_end([1, 2, 3]))
# print(add_end(['x', 'y', 'z']))
#
# print(add_end()) # ['END']
# print(add_end()) # ['END','END']
# print(add_end()) # ['END','END','END']

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
# print(add_end()) # ['END']
# print(add_end()) # ['END']
# print(add_end()) # ['END']

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc([1,2,3]))
# print(calc((1,3,5,7)))

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc(1,2))
# print(calc(*[1,2,3]))

# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
# person('Adam', 45, gender='M', job='Engineer')
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)

# 命名关键字参数
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)
#
# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# def person(name, age, *, city, job):
#     print(name, age, city, job)
#
# person('Jack', 24, city='Beijing', job='Engineer')

# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
#
# person('Jack', 24, 'Beijing', 'Engineer')

# def person(name, age, *, city='Beijing', job):
#     print(name, age, city, job)
#
# person('Jack', 24, job='Engineer')

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def product(*nums):
    sum = 1
    if nums == ():
        raise TypeError('Empty Input')
    for num in nums:
        if not isinstance(num, (int, float)):
            raise TypeError("bad operand type")
        sum = sum * num
    return sum

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


