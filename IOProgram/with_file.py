#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# open file
# f = open('./notfound.txt', 'r') #IOError

# f = open('./test.txt', 'r')
# print(f.read())
# f.close()
# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的

# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with语句来自动帮我们调用close()方法

# with open('/path/to/file', 'r') as f:
#     print(f.read())

# read(size)每次最多读取size个字节
# readline()可以每次读取一行内容
# readlines()一次读取所有内容并按行返回list

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

# with open('./test.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip()) # 把末尾的'\n'删掉

# 二进制文件 rb
# f = open('./test.jpg', 'rb')
# print(f.read())

# 字符编码
# f = open('./gbk.txt', 'r', encoding='gbk')
# print(f.read())
#
# # UnicodeDecodeError 存在非法编码字符 errors='ignore'
# f = open('./gbk.txt', 'r', encoding='gbk', errors='ignore')

# write file
# f = open('./test.txt', 'w')
# f.write('Hello, world!')
# f.close()

# with open('./test.txt', 'w') as f:
#     f.write('Hello, world!')

# w：覆盖 a：追加

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

