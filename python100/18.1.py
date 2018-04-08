m = int(input('number='))
n = int(input('qu='))
num = 0
sum = 0
for i in range (0,n+1):
    num += m*(10 ** i)
    sum += num
#    print(num)
print(sum)