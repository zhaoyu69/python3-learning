#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DOM vs SAX 操作XML
# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

# SAX解析器读到一个节点时产生3个事件
# 1. start_element 左标签
# 2. char_data 标签包裹内容
# 3. end_element 右标签

# from xml.parsers.expat import ParserCreate
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

# test
from xml.parsers.expat import ParserCreate
from urllib import request

class DefaultSaxHandler(object):
    weather = {}
    def weather_forecast(self, name, attrs):
        if name == 'yweather:location':
            self.weather['city'] = attrs['city']
        #打印天气预报
        if name == 'yweather:forecast':
            print('weather:{:^13}, date:{}, low:{}, high:{}'.format(attrs['text'], attrs['date'], attrs['low'], attrs['high']))

def parseXml(xml_str):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.weather_forecast
    parser.Parse(xml_str)
    return handler.weather

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
