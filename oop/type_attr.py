#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print(type(123))
# print(type('str'))
# print(type(None))
# print(type(abs))
#
# import types
#
# def fn():
#     pass
#
# print(type(fn)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x: x)==types.LambdaType)
# print(type((x for x in range(10)))==types.GeneratorType)
#
# # isinstance
# # 判断是两者的其一
# isinstance((1, 2, 3), (list, tuple))

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 获取一个对象的所有属性和方法
print(dir('ABC'))

class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
         return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x')) # 有属性'x'吗?

setattr(obj, 'y', 19) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
getattr(obj, 'y') # 获取属性'y'
print(obj.y)

getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print(fn)
print(fn())