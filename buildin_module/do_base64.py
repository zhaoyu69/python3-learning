#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# base64
import base64
# print(base64.b64encode(b'binary\x00string'))
# print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
# print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64decode('abcd--__'))

def safe_base64_decode(s):
    s = s + len(s) % 4 * (b'=')
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
