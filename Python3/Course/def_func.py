# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
        print("bad type")
    elif b**2 - 4*a*c >= 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
        return (x1,x2)
    else:
        return "no result"


print(quadratic(1, -1, 4))