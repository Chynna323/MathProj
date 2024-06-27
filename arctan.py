# -*- coding: utf-8 -*-
#!usr/bin/python
import sys

x = 0.25
TOL = 0.001 
M = 1000
series = 0.0
N = 0

while N < M:
    term = (pow(x, 2*N+1)*pow(-1,N))/(2*N+1)
    series += term
    N+=1
    
    if abs(term) < TOL:
        print('arctan(', x, ') is approximately =', series)
        print('In ', N, ' iterations.')
        sys.exit()
print('Method Failed in ', M, ' iterations.')