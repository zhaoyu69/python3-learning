#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 内置 sqlite3

# import sqlite3
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# print(cursor.rowcount)
# cursor.close()
# conn.commit()
# conn.close()

# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('select * from user where id=?', ('1',))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()

# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

# test
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select * from user where score between ? and ? order by score', (low, high))
    values = cursor.fetchall()
    return list(map(lambda x:x[1], values))
    cursor.close()
    conn.close()

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')

