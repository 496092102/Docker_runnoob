#题目：输入三个整数x,y,z，请把这三个数由小到大输出。

x = input('x=')
y = input('y=')
z = input('z=')

if x >= y:
    m = x
    x = y
    y = m
if x >= z:
    m = x
    x = z
    z = m
if y >= z:
    m = y
    y = z
    z = m

print(x,y,z)