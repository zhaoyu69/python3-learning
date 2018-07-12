#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from enum import Enum
# # Month类型的枚举类
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# # 引用一个常量
# print(Month.Jan)
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# @unique装饰器可以帮助我们检查保证没有重复值。
# from enum import Enum, unique
#
# @unique
# class Weekday(Enum):
#     Sun = 0  # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6

# test
from enum import Enum, unique

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
