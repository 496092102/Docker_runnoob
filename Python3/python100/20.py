#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下
#求它在第10次落地时，共经过多少米？第10次反弹多高？
h = 100
si = 0
for i in range(1,11):
    if i == 1:
        si = h
    else:
        si = si + 2*h
    h = h/2
    print(i,h)
print(si)


