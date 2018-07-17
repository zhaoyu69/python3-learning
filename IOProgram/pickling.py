#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 序列化
# import pickle
# d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()
# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# JSON
# import json
# d = dict(name='Bob', age=20, score=88)
# print(json.dumps(d)) # <class 'str'>
#
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str)) # <class 'dict'>

# JSON进阶
import json

# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# s = Student('Bob', 20, 88)
# print(json.dumps(s)) # TypeError

# class -> {}
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
#
# print(json.dumps(s, default=student2dict))

# class的__dict__就是一个dict，用来存储实例变量
# print(json.dumps(s, default=lambda obj: obj.__dict__))

# loads也需要函数转换
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
#
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str, object_hook=dict2student)) # 反序列化的Student实例对象

# test
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)

print(s)