#题目：求s=a+aa+aaa+aaaa+aa...a的值
# 其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
m = int(input('number='))
n = int(input('qu='))
num = 0
sum = 0
for i in range (0,n+1):
    num += m*(10 ** i)
    sum += num
#    print(num)
print(sum)


