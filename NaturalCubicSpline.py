# -*- coding: utf-8 -*-
"""
@author: chynna
"""
#~~~Imports~~~~~
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import kn

'''Inputs: number x0...xn, values f(x0)...f(xn), and f'(x0)...f'(xn)

Outputs: Q0,0 Q1,1... Q2n+1,2n+1 ; where Qs are the coeffiecients of the Hermite polynomial.

Algorithm 3.4 page 147 & 3.5 page 152
'''
#Not error checking make sure your arrays have the same length!    
x_vals = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
y_vals = np.array([1.62484, 1.04283, 0.70199, 0.48874, 0.34884, 0.25376])
fpo = -3.85158
fpn = -0.39362
n = len(x_vals)


def NatCubicSpline(x,a):
    h, alpha, mu, l, z, c, b, d = np.zeros((8, n))
    #step 1
    for i in range(n-1):
        h[i] = x[i+1] - x[i]
        #Step 2
    for i in range (1, n-1):
        alpha[i] =((3/h[i]) * (a[i+1] - a[i])) -((3/h[i-1]) * (a[i]-a[i-1]))
        
    '''Steps 3-5 and part of 6 solve a tridiagonal linear system using a method described in 6.7'''
        
    #Step 3
    l[0] = 1
    mu[0] = 0
    z[0] = 0
    #Step 4
    for i in range(1, n-1):
        l[i] = 2*(x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]
    #Step 5
    l[n-1] = 1
    z[n-1] = 0
    c[n-1] = 0    
    #Step 6
    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1] + 2*c[j])/3
        d[j] = (c[j+1] - c[j]) / (3*h[j])
    a = a[:n-1]
    b = b[:n-1]
    c = c[:n-1]
    d = d[:n-1]
    return a, b, c, d
  
    
def ClampCubicSpline(x, a, fpo, fpn):
    h, alpha, mu, l, z, c, b, d = np.zeros((8, n))
    #step 1
    for i in range(n-1):
        h[i] = x[i+1] - x[i]
    #Step 2
    alpha[0] = 3*(a[1] - a[0])/h[0] - 3*fpo
    alpha[n-1] = 3*fpn - 3*(a[n-1] - a[n-2])/h[n-2]

    #Step 3
    for i in range(1, n-1):
        alpha[i] = (3/h[i]) * (a[i+1] - a[i]) - (3/h[i-1]) * (a[i] - a[i-1])

    #Step 4        
    l[0] = 2*h[0]
    mu[0] = 0.5
    z[0] = alpha[0]/l[0]
    
    for i in range(1, n-1):
        l[i] = 2*(x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1])/l[i]
    l[n-1] = h[n-2] * (2 - mu[n-2])
    z[n-1] = (alpha[n-1] - h[n-2] * z[n-2])/l[n-1]
    c[n-1] = z[n-1]
       
    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = ((a[j+1] - a[j])/h[j]) - (h[j]/3)*(c[j+1] + 2*c[j])
        d[j] = (c[j+1] - c[j])/(3*h[j])
    
    a = a[:n-1]
    b = b[:n-1]
    c = c[:n-1]
    d = d[:n-1]
    
    return a, b, c, d
  
def CalcCubicSpline(a, b, c, d, x, approx):
    n = len(x)
    if type(approx) == float:  
        approx = [approx]
    m = len(approx)
    sy = np.zeros(m)
    for j in range(n-1):
        for i in range(m):
            #print(j,i)
            if x[j] <= approx[i] <= x[j+1]:
                sy[i] = a[j] + b[j]*(approx[i] - x[j]) + c[j]*(approx[i] - x[j])**2 + d[j]*(approx[i] - x[j])**3
                #print(a[j], b[j], c[j], d[j], x[j],approx[i])
    return sy



a, b, c, d = ClampCubicSpline(x_vals, y_vals, fpo, fpn)
print("a=", a,"\nb=",b,"\nc=",c,"\nd=",d)

# Data for plotting
t = np.arange(1.0, 2.0, 0.05)
k = kn(2,t)
b = CalcCubicSpline(a, b, c, d, x_vals, t)


fig, ax = plt.subplots()
ax.plot(t, k,'-', label ='Bessel Func')
ax.plot(t, b,'--', label = 'Clamped Cubic')
ax.set(xlabel='x', ylabel='y',
       title='Clamped Cubic Spline')
ax.grid()

fig2, ax2 = plt.subplots()
ax2.plot(t, abs(k-b), label = 'Clamped Cubic Error')
ax2.grid
ax2.set(xlabel='x', ylabel='y',
       title='Clamped Cubic Error')
fig2.savefig("ClaSplineErr.png")
fig.savefig("ClaSpline.png")
plt.show()