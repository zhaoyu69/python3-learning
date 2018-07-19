#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# virtualenv: 为每个应用创建一套“隔离”的Python运行环境。

# pip3 install virtualenv

# 整一套独立的python运行环境

# 1. 创建目录
# mkdir myproject
# cd myproject/

# 2. 创建一个独立的Python运行环境，命名为venv
# virtualenv --no-site-packages venv
# --no-site-packages 不带任何第三方包

# 进入环境
# source venv/bin/activate
# venv\Scripts\activate.bat (Windows)

# 退出环境
# deactivate