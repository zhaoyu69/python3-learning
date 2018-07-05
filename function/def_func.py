#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def my_abs(x):
#     # 参数类型检查
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print(my_abs(-99))
#
# def nop():
#     pass

# import math
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)
#
# r = move(100, 100, 60, math.pi / 6)
# print(r) # tuple

import math

def quadratic(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise TypeError('bad operand type')
    r = b*b - 4*a*c
    if r < 0:
        return
    elif r == 0:
        x = -1 * b / 2 * a
        return x
    else:
        x1 = (-1 * b + math.sqrt(r)) / (2 * a)
        x2 = (-1 * b - math.sqrt(r)) / (2 * a)
        return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
print('quadratic(2, 4, 2) =', quadratic(2, 4, 2))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
elif quadratic(2, 4, 2) != (-4.0):
    print('测试失败')
else:
    print('测试成功')