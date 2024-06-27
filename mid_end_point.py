# -*- coding: utf-8 -*-
"""


@author: chynna
"""
import numpy as np

h = 0.2
f = np.array([1.62484, 1.04283, 0.70199, 0.48874, 0.34884, 0.25376])

   
#Three Endpoint
#y'(1.0)
print("3-Endpoint y'(1.0) =", (-3*f[0]+4*f[1]-f[2]/(2*h)))

#y'(1.2)
print("3-Endpoint y'(1.2) =", (-3*f[1]+4*f[2]-f[3]/(2*h)))
#y'(1.4)
print("3-Endpoint y'(1.4) =", (-3*f[2]+4*f[3]-f[4]/(2*h)))
#y'(1.6)
print("3-Endpoint y'(1.6) =", (-3*f[3]+4*f[4]-f[5]/(2*h)), "\n\n")

#Three Midpoint
#y'(1.2)
print("3-Midpoint y'(1.2) =", (f[2]-f[0])/(2*h))
#y'(1.4)
print("3-Midpoint y'(1.4) =", (f[3]-f[1])/(2*h))
#y'(1.6)
print("3-Midpoint y'(1.6) =", (f[4]-f[2])/(2*h))
#y'(1.8)
print("3-Midpoint y'(1.8) =", (f[5]-f[3])/(2*h), "\n\n")

#Five Endpoint
#y'(1.0)
print("5-Endpoint y'(1.0)=", (-25*f[0]+48*f[1]-36*f[2]+16*f[3]-3*f[4])/(12*h))
#Five Endpoint
#y'(1.2)
("5-Endpoint y'(1.0)=", (-25*f[1]+48*f[2]-36*f[3]+16*f[4]-3*f[5])/(12*h))
#y'(1.4)
print("5-midpoint y'(1.4)=", (f[0]-8*f[1]+8*f[3]-f[4])/(12*h))
#y'(1.6)
print("5-midpoint y'(1.6)=", (f[1]-8*f[2]+8*f[4]-f[5])/(12*h))
#Five Endpoint
#y'(1.8)
print("5-Endpoint y'(1.8)=", (-25*f[4]+48*f[3]-36*f[2]+16*f[1]-3*f[0])/(12*h))
#y'(2.0)
print("5-Endpoint y'(2.0)=", (-25*f[5]+48*f[4]-36*f[3]+16*f[2]-3*f[1])/12*h)

#f(x) = 3x**1/3
x0 = 17
for i in range(1, 21):
    x = ((3*(x0+10**(-i))**(1/3))-(3*x0**(1/3)))/(10**(-i))
    print("3*(17)^(1/3) at i =", i, "\n", x, "\n\n")
    