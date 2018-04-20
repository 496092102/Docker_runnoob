# 有一对兔子，从出生后第 3个月 起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 
def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)

for i in range(0,10):
    print(2*f(i))
