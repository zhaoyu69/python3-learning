#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re


class MyHTMLParser(HTMLParser):
    a_t1 = False
    a_t2 = False
    a_t3 = False
    def __init__(self):
        HTMLParser.__init__(self)
        self.information = []
        self.information_all = {}


    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        if tag=="time" :
            self.a_t1 = True
        elif tag=="span" and _attr(attrs, 'class')=="event-location":
            self.a_t2 = True
        elif tag=="h3" and _attr(attrs, 'class')=="event-title":
            self.a_t3 = True


    def handle_data(self, data):
        if self.a_t1 is True:
            if re.match(r'^\s\d{4}', data):
                self.information.append(dict(year=data))
            else:
                self.information.append(dict(day=data))
        elif self.a_t2 is True:
            self.information.append(dict(event_location=data))
        elif self.a_t3 is True:
            self.information.append(dict(event_title=data))


    def handle_endtag(self, tag):
        if tag == "time":
            self.a_t1 = False
        elif tag =="span":
            self.a_t2 = False
        elif tag == "h3":
            self.a_t3 = False



def parseHTML(html_str):
    parser = MyHTMLParser()
    parser.feed(html_str)
    for i, val in enumerate(parser.information):
        i +=  1
        print(val)
        if i%4==0:

            print('--------------------------------------------')


URL = 'https://www.python.org/events/python-events/'
with request.urlopen(URL, timeout=4) as f:
    data = f.read()

parseHTML(data.decode('utf-8'))