#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3
#编程找出1000以内的所有完数。
#1、求因子函数
#2、判断是否为完数
#判断数是否为素数（质数prime）
for i in range(3,20):
    for j in range(2,i):
        if i % j == 0:
            break
        else:
            print(i)
        
