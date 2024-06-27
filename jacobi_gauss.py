# -*- coding: utf-8 -*-
"""
@author: chynna

"""

import numpy as np
Atest = np.array([[10,-1,2, 0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]]) 
A1 = np.array([[10,5,0, 0],[5,10,-4,0],[0,-4,8,-1],[0,0,-1,5]])
A2 = np.array([[4,1,-1,1],[1,4,-1,-1],[-1,-1,5,1],[1,-1,1,5]])
n = 4
b = [6, 25, -11, 15]
b2 = [2, -1, 0, 1]
XO = np.zeros(n)
TOL = 10**(-3)
iterations = 15
#%%
def Jacobi(a, b, n, x_0, tol,iter):
    x = x_0.copy()
    k = 1
    sum = x.copy()
    while(k <= iter):
        for i in range(n):
            for j in range(n):
                if j != i:
                    sum[i] = sum[i] + a[i,j]*x[j]
                    
            x[i] = (b[i]-sum[i])/a[i,i]
            sum[i]=0
        print("iteration: ", k)
        print("x1\tx2\tx3\tx4")
        print(x)
        #print(np.linalg.norm((x - x_0), ord=np.inf))
        if np.linalg.norm((x - x_0), ord=np.inf) < tol:
            
            print("Solution found after ", k, "iterations.")
            return x
        k = k + 1
        x_0 = x.copy()
    print("Max iterations", iter, " has been exceeded for tolerance:", tol)
    return x

print("Jacobi Result\n", Jacobi(A1,b,n,XO,TOL,iterations))

#%%
def Gauss_Seidel(a, b, n, x_0, tol, iter):
        x = x_0.copy()
        sum1 = np.zeros(n)
        sum2 = np.zeros(n)
        k = 1
        while k <= iter:
            for i in range(n):
                for j in range(i):
                    sum1[i] = sum1[i] + a[i, j] * x[j]
                for j in range(i + 1, n):
                    sum2[i] = sum2[i]+ a[i, j] * x_0[j]
                x[i] = (b[i] - sum1[i] - sum2[i]) / a[i, i]
                sum1[i] = 0
                sum2[i] = 0
            print("iteration: ", k)
            print("x1\tx2\tx3\tx4")
            print(x)   
            #print(np.linalg.norm((x - x_0), ord=np.inf))
            if np.linalg.norm(x - x_0, ord=np.inf) < tol:
                print("Solution found after ", k, "iterations.")
                return x
            k += 1
            x_0 = x.copy()
        print("Max iterations", iter, "has been exceeded")
        return x
print("Gauss_Seidel result\n", Gauss_Seidel(A2,b2,n,XO,10**(-5),30))