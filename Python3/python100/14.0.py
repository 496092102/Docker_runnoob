#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
def pri(m):
    for n in range(2,m):
        if (m % n != 0):
            return m
i = int(input('Give me a number:'))
for i in range(1,100):
    k = pri(i)
    print(k)