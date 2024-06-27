# -*- coding: utf-8 -*-
"""
@author: chynna
"""
#~~~Imports~~~~~
import matplotlib.pyplot as plt
from scipy.special import kn
import numpy as np

'''Inputs: number x0...xn, values f(x0)...f(xn), and f'(x0)...f'(xn)

Outputs: Q0,0 Q1,1... Q2n+1,2n+1 ; where Qs are the coeffiecients of the Hermite polynomial.

Algorithm 3.3 page 139
'''
#~~~FUNCTIONS~~~
#Hermite calculates your Q coefficients, and returns the entire Q matrix with the z duplicate for later calculation
def Hermite(x, y, fp):
    n = len(x)
    z = np.zeros((2*n+1))
    q = np.zeros((2*n+1, 2*n+1))
    #Step 1, for i=0...n do steps 2 and 3

    for i in range(n):
        #Step 2
        z[2*i] = x[i]
        z[2*i+1] = x[i]
        q[2*i,0] = y[i]
        q[2*i+1,0] = y[i]
        q[2*i+1, 1] = fp[i]
        
        #Step 3
        if i != 0:
            q[2*i, 1] = (q[2*i, 0] - q[2*i-1, 0]) / (z[2*i]-z[2*i-1])
            '''Practice prints, walks through the equation above
            print("i=", i)
            print("q[2*i, 0] - q[2*i-1, 0]",q[2*i, 0] - q[2*i-1, 0])
            print("z[2*i]-z[2*i-1]",z[2*i]-z[2*i-1])
            print("Q[2*i,1]",q[2*i,1])'''

            
    #Step 4
    for i in range(2, 2*n):
        for j in range(2, i+1):
            q[i, j] = (q[i, j-1] - q[i-1, j-1]) / (z[i]-z[i-j])
    for i in range(2*n+1):
        #Lists your calculated coeffs
        print("Q[",i,",",i,"]=", q[i,i])
    return q, z

'''
Function to calculate Hermite polynomials with found coefficients
    *Starts off by setting your answer to q[0,0] which is just f[x1]
    *Each for loop iteration calculate Q[1,1](x-x0).....Q[2n+1,2n+1](x-x0^2)***(x-xn-1)^2(x-xn)
    *Since z contains a dounle of the x values, I run through that to do the squares
'''
def CalcH(q, approx, z):
    val = q[0,0]
    for i in range(1, len(z)):
        u = 1
        for j in range(i):
            u *= (approx - z[j])
            #This is your (x-x0)...stuff
        val += u * q[i,i]
    return(val)

#Not error checking make sure your arrays have the same length!    
x_vals = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
y_vals = np.array([1.62484, 1.04283, 0.70199, 0.48874, 0.34884, 0.25376])
fp_vals= np.array([-3.85158, -2.17264, -1.32368, -0.85156, -0.57022, -0.39362])


q, z = Hermite(x_vals, y_vals, fp_vals)
print(CalcH(q,1.7,z))
    

# Data for plotting
t = np.arange(0.5, 2.5, 0.01)
k = kn(2,t)
b = CalcH(q, t, z)
fig, ax = plt.subplots()
ax.plot(t, k,'-', label ='Bessel Func')
ax.plot(t, b,'--', label = 'Hermite Approx')
ax.set(xlabel='x', ylabel='y',
       title='Hermite Interpolation')
ax.grid()


fig2, ax2 = plt.subplots()
ax2.plot(t, abs(k-b), label = 'Hermite Error')
ax2.grid
ax2.set(xlabel='x', ylabel='y',
       title='Hermite Error')
fig2.savefig("Hermite_abs_err.png")
fig.savefig("hermite.png")
plt.show()

