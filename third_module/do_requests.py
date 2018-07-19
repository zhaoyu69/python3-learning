#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install requests

import requests
# r = requests.get('https://www.douban.com/') # 豆瓣首页
# print(r.text)

# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# print(r.url)
# print(r.encoding)
# print(r.content)

# get json
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

# set headers
# r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)

# post
# r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# requests默认使用application/x-www-form-urlencoded，可直接传json参数
# params = { "key": "value" }
# r = requests.post(url, json=params) # 内部自动序列化为JSON

# 上传文件
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)

# put(), delete(), ...

# get headers
# print(r.headers)
# print(r.headers['Content-Type'])
# get cookies
# print(r.cookies['ts'])

# requests传入cookies
# cs = {'token': '12345', 'status': 'working'}
# r = requests.get(url, cookies=cs)

# 指定超时
# r = requests.get(url, timeout=2.5) # 2.5秒后超时