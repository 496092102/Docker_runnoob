# 打印出所有的"水仙花数"
# "水仙花数"是指一个三位数，其各位数字立方和等于该数本身
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
#!/usr/bin/python
# -*- coding: UTF-8 -*-
for x in range(0,10):
    for y in range(0,10):
        for z in range(0,10):
            m = x**3 + y**3 + z**3
            n = 100 * x+ 10 * y + z
            if (m == n):
                print(m,'\t',x,y,z)