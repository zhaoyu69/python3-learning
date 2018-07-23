#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 安装mysql并配置

# 安装mysql驱动
# pip install mysql-connector
# pip install mysql-connector-python-rf==2.2.2

import mysql.connector
conn = mysql.connector.connect(user='root', password='password', database='test')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()