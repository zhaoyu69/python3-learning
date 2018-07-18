#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取当前日期和时间
# from datetime import datetime
# now = datetime.now() # 获取当前datetime
# print(now)
# print(type(now))
#
# dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
# print(dt)
#
# # datetime转换为timestamp 浮点数(s) 小数位表示ms
# st = dt.timestamp() # 把datetime转换为timestamp
# print(st)
#
# # timestamp转换为datetime
# dt1 = datetime.fromtimestamp(st)
# print(dt1)
#
# dt2 = datetime.utcfromtimestamp(st) # UTC时间
# print(dt2)

# # str转换为datetime
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)
#
# # datetime转换为str
# cstr = datetime.now().strftime('%a, %b %d %H:%M')
# print(cstr)

# datetime加减
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now)
# print(now + timedelta(hours=10))
# print(now - timedelta(days=1))
# print(now + timedelta(days=2, hours=12))

# # 本地时间转换为UTC时间
# from datetime import datetime, timedelta, timezone
# tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
# print(dt)
#
# # 时区转换 任何带时区的datetime都可以转换
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)
# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)

import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    # ->local
    local_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # ->utc
    re_utc = re.compile(r'^UTC([+-]\d+?):00$')
    groups = re_utc.match(tz_str).groups()
    hours = int(groups[0])
    tz_utc_8 = timezone(timedelta(hours=hours)) # 创建时区
    utc_dt = local_dt.replace(tzinfo=tz_utc_8)
    # 返回utc的timestamp
    return utc_dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')