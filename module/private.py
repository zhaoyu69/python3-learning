#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。