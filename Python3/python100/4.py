#题目：输入某年某月某日，判断这一天是这一年的第几天？
#程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
i = int(input("年"))
j = int(input("月"))
k = int(input("日"))

for l in range(1,j):
    if l in (1,3,5,7,8,10,12) :
        m = 31
    elif l != 2:
        m = 30
    elif (i%400 == 0) or (i%100 != 0 and i%4 == 0):
        m = 29
    else:
        m = 28
    k += m
#    print(m)
print("it is the %dth day" % k)

