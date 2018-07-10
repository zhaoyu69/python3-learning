#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Student(object):
#     pass
#
# # 给实例绑定属性和方法
# s = Student()
# s.name = 'Michael'
# print(s.name)
#
# def set_age(self, age):
#     self.age = age
#
# from types import MethodType
# s.set_age = MethodType(set_age, s)
# s.set_age(25)
# print(s.age)
#
# # 给实例绑定方法，对另一个实例不起作用
# s2 = Student()
# # print(s2.name)
# # s2.set_age(30)
#
# # 给所有实例都绑定方法，可以给class绑定方法
# def set_score(self, score):
#     self.score = score
#
# Student.set_score = set_score
# s.set_score(100)
# s2.set_score(99)
# print(s.score)
# print(s2.score)

# __slots__:限制实例的属性
# 比如，只允许对Student实例添加name和age属性。

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'zysoft'
s.age = 23
s.score = 100

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99
