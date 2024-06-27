# -*- coding: utf-8 -*-

#!/usr/bin/python
import math   # This will import math module


#Define our fuction
def f(x):
    """
    -x*e^x
    -ln(4)
    -tan(x)
    """
    #return x*math.exp(x)-2
    #return idk
    return math.tan(x)
"""#Apparently this is called the fast convergent method
And it can be used to estimate ln(4) since i can't actually calculate ln(4) since I am meant to be approximatiing. I just need it to be accurate up to 10^-8 and then I will be okay... maybe..."""

#PLEASE CHECK YOUR INPUTS, I'M NOT CODING ERROR CATCHING!!

#~~~~~Start Bisection Method~~~~~

def bisection(a, b, err):
    iteration = 1
    print("\n Bisection Method with Steps Printed out\n")
    test = True
    
    while (test and iteration<1000):
        #find midpoint and return the value of F(mid)
        mid = (a + b)/2
        print('Iteration:%d, mid = %0.10f and f(mid) = %0.10f' % (iteration, mid, f(mid)))
        
        #Determine next interval
        if f(a) * f(mid) < 0:
           b = mid
        else:
           a = mid
        #Increment and check if we are at our errorbound
        iteration += 1
        test = abs(f(mid)) > err
        
        
#Time to get our inputs
a = float(input('First Guess: '))
b = float(input('Second Guess: '))
err = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and bisecting
#Can't use this if our func doesn't cross the x-axis.

if f(a) * f(b) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(a,b,err)