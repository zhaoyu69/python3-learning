#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1.print打印有问题的变量
# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()

# 2.断言（assert代替print）
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     foo('0')

# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError

# python -0 err.py 使用-0参数屏蔽文件所有的assert

# 3.logging
# 和assert比，logging不会抛出错误，而且可以输出到文件
# import logging
# logging.basicConfig(level=logging.INFO)
#
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# 它允许你指定记录信息的级别，有debug，info，warning，error等几个级别

# 4.启动Python的调试器pdf
# 让程序以单步方式运行，可以随时查看运行状态。
# s = '0'
# n = int(s)
# print(10 / n)

# python -m pdb err.py
# pdb命令 l:查看代码 n:单步执行代码 p 变量名:查看变量 q:结束调试 c:继续运行

# 5.pdb.set_trace()
# 不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点

# import pdb
#
# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# print(10 / n)

# 6.IDE