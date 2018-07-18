#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# namedtuple 保持tuple的不变性，又可以根据属性来引用
from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x, p.y)
# print(isinstance(p, Point))
# print(isinstance(p, tuple))

# Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque 高效实现插入和删除操作的双向列表，适合用于队列和栈
# append, appendleft, pop, popleft
# from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)

# defaultdict key不存在时的默认值
# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

# OrderedDict 保持key的顺序，按插入顺序排列
from collections import OrderedDict
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od)

# od = OrderedDict()
# od['z'] = 1
# od['y'] = 2
# od['x'] = 3
# print(od.keys())

# 先进先出的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] += 1
print(c)