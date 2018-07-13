#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
# print(os.name) # 操作系统类型
# # print(os.uname()) # window不提供
# print(os.environ) # 环境变量
# print(os.environ.get('PATH')) # 环境变量PATH的值

# # 查看当前目录的绝对路径:
# print(os.path.abspath('.'))
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.path.join('.', 'testdir'))
# # 然后创建一个目录:
# os.mkdir('./testdir')
# # 删掉一个目录:
# os.rmdir('./testdir')
#
# # 合并或拆分路径，不要直接拆字符串，使用os.path.join() | os.path.split()
# print(os.path.split('./testdir/file.txt'))
#
# # os.path.splitext()得到文件扩展名
# print(os.path.splitext('./testdir/file.txt'))
#
# # 重命名文件:
# os.rename('test.txt', 'test.py')
# # 删除文件:
# os.remove('test.py')

# # 列出当前目录下所有目录:
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# # 列出所有的.py文件
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

