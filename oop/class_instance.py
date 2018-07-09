#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    # 特殊方法“__init__”前后分别有两个下划线！！！
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print(bart)
print(Student)

bart.name = 'ssssss'
print(bart.name)
print(bart.score)


# def print_score(std):
#     print('%s: %s' % (std.name, std.score))
# print_score(bart)

bart.print_score()
print(bart.get_grade())


