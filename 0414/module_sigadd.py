# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:46:29 2021

@author: nicholas
"""
import numpy as np

def sigadd(n1,x1,n2,x2):
    nk=np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1)
    N=len(nk)
    y1=np.zeros(N) # -5~15까지 21개의 0 배열
    y2=np.zeros(N)
    aa=abs(min(min(n1),min(n2)))
    n1=n1+aa # +5를 하는 이유는? n2가 -5~7까지의 값, 이를 19행에서 인덱스로 사용, -면 인덱스 불가
    n2=n2+aa
    print("n1", n1)
    print("n2", n2)
    y1[int(min(n1)):int(max(n1)+1)]=x1 # 0~15까지 zeros배열에 값 대입
    y2[int(min(n2)):int(max(n2)+1)]=x2 # 1~7까지 zeros배열에 값 대입
    y=y1+y2 # Signal Addition
    return nk,y,y1,y2

def sigmult(n1,x1,n2,x2):
    n=np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1)
    N=len(n)
    y1=np.zeros(N)
    y2=np.zeros(N)
    aa = abs(min(min(n1), min(n2)))
    y1[min(n1)+aa: max(n1)+aa+1] = x1    
    y2[min(n2)+aa: max(n2)+aa+1] = x2
    y=y1.T*y2
    return n,y,y1,y2

def sigfold(n1,x1):
    N=len(n1)
    y=np.zeros(N)
    n=np.zeros(N)
    for i in range(N):
        y[i] = x1[N-1-i]
        n[i] = -1*n1[N-1-i]
    return n, y