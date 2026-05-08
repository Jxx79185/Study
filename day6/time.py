import os
import sys
import time
import datetime
# print(sys.argv)
# 转换为本地时间的字符串
print(os.stat('day6/time.py'))
print(time.localtime())
atime_str = time.strftime("%Y-%m-%d %X ", time.localtime(os.stat('day6/time.py').st_atime))
mtime_str = time.strftime("%Y-%m-%d %X", time.localtime(os.stat('day6/time.py').st_mtime))
ctime_str = time.strftime("%Y-%m-%d %X", time.localtime(os.stat('day6/time.py').st_ctime))
print("最后访问时间:", atime_str)
print("最后修改时间:", mtime_str)
print("创建时间:", ctime_str)
print(datetime.datetime.fromtimestamp(os.stat('day6/time.py').st_ctime))
print(time.time())
print(time.localtime())
print(datetime.datetime.now())
