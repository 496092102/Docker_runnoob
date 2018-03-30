#题目：暂停一秒输出，并格式化当前时间。
import time,datetime
#now = time.time()
now = datetime.datetime.strptime
print(now)
som = time.localtime(now)
print(som)
str = time.strftime('%Y-%m-%d %H:%M:%S', som)
print(str)