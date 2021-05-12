# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:46:19 2021

@author: nicholas
"""
import numpy as np

def impseq(n0, n1, n2):
    N = n2 - n1 + 1
    n = np.arange(N)
    xn = np.zeros(N)
    for i in range(N):    
        if (i+n1) == n0: xn[i]=1
    return xn

def stepseq(n0, n1, n2):
    N=n2-n1+1
    n = np.arange(N)
    xn = np.zeros(N)
    for i in range(N):   
        if (i+n1) >= n0: xn[i]=1
    return xn

def sigadd(n1,x1,n2,x2):
    nk = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2))+1)
    N = len(nk)
    y1 = np.zeros(N)
    y2 = np.zeros(N)
    aa = abs(min(min(n1), min(n2)))
    n1 = n1 + aa
    n2 = n2 + aa
    y1[int(min(n1)):int(max(n1)+1)] = x1
    y2[int(min(n2)):int(max(n2)+1)] = x2
    y = y1 + y2
    return nk, y, y1, y2

def sigmult(n1, x1, n2, x2):
    n=np.arange(min(min(n1), min(n2)), max(max(n1), max(n2))+1)
    N = len(n)
    y1 = np.zeros(N)
    y2 = np.zeros(N)
    aa = abs(min(min(n1), max(n1), min(n2), max(n2)));
    y1[min(n1)+aa : max(n1)+aa+1] = x1
    y2[min(n2)+aa : max(n2)+aa+1] = x2
    y = y1.T * y2
    return n,y,y1,y2

def sigshift(m, x, k):
    n = m + k
    y = x
    return n, y

def sigfold(n1, x1):
    N = len(n1)
    y = np.zeros(N)
    n = np.zeros(N)
    for i in range(N):
        y[i] = x1[N-1-i]
        n[i] = -1*n1[N-1-i]
        return n,y
    
