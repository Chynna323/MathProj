# -*- coding: utf-8 -*-
"""

@author: chynna
"""
import math

#page 205, thrm 4.5
#n is even
def CompositeTrap(f, a, b, n):
    if n%2 == 0:
        x = a
        h = (b-a)/n
        t = f(a) + f(b)
        for i in range(1, n):
            x += h
            t += 2 * f(x)
            return t * (h/2)
    else:
        return 'n should be even positive integer'
#algorithm 4.1 page 205
#n is even
def CompositeSimpson(f, a, b, n):

    if n%2 == 0:
        h = (b-a)/n
        xi0 = f(a) + f(b)
        xi1 = 0
        xi2 = 0

        for i in range(n-1):
            x = a + i*h
            if i%2==0:
                xi2 = xi2+f(x)
            else:
                xi1 = xi1+f(x)
            xi = (xi0 + 2*xi2 +4*xi1)
            return xi * (h / 3)
    else:
        print("n should be a positive even integer, try again")
        return 0
    
def f(x):
    return math.sin(x**(8/3))
    # return math.cos(x**(14/3))

print("Composite Trapezoidal: ", CompositeTrap(f, 0, math.pi,678))
# print("Composite Simpson: ", CompositeSimpson(f, 0, 2*math.pi,134))