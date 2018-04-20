#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
i = float(input('Give me a number:'))
if i >= 90:
    print('A')
#elif i <90 and i >= 60:
elif i >= 60:
    print('B')
else:
    print('C')