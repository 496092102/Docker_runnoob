#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
i = str(input('Give me a str:'))
m = len(i)
for k in range(0,m):
    print(i[k])
    if i[k] in range('a','z'):
        x += 1
    elif i[k] == ' ':
        y += 1
    elif i[k] in range(0,10):
        z += 1
    else:
        w += 1
print(x,y,z,w)
