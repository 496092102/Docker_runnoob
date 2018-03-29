#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
for i in range(0,200):
    for j in range(0,200):
        if (i*i >= 100 and j*j >= 268 and (i*i + 168) == j*j):
            print(i,j)
            print(i*i - 100)

