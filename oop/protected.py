#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Student(object):
#     # 实例的变量名如果以__开头，就变成了一个私有变量（private）
#     # 只有内部可以访问，外部不能访问
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')
#
# bart = Student('zysoft', 99)
# print(bart.get_name())
# print(bart.get_score())
#
# bart.set_score(100)
# print(bart.get_score())

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender = gender

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')