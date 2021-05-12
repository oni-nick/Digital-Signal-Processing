# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:39:58 2021

@author: nicholas
"""

import numpy as np
import matplotlib.pyplot as plt
from module_sigadd import *


n1=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # 16개
x1=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1]) # 16개
n2=np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]) # 13개
x2=np.array([1,2,3,4,5,6,7,6,5,4,3,2,1]) # 13개
# 5. folding
nx=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
x=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1])
ny, y =sigfold(nx, x)
print("nx=",nx); print("x=",x); print("ny=", ny); print("y=",y)


# plotting
n,y,zx1,zx2 = sigadd(n1,x1,n2,x2); print("y(n)=",y)
print("x1(n)=", zx1); print("x2(n)=", zx2); print("n=", n)
plt.figure(1)
plt.subplot(3,1,1); plt.stem(n,zx1, "blue"); plt.grid()
plt.ylabel("x1(zx1)"); plt.title("Signal Addition")
plt.subplot(3,1,2); plt.stem(n,zx2, "blue"); plt.grid(); plt.ylabel("x2(zx2)");
plt.subplot(3,1,3); plt.stem(n,y, "blue"); plt.grid(); 
plt.xlabel("n"); plt.ylabel("y1=x1+x2")

n,y,zx1,zx2 = sigmult(n1,x1,n2,x2); print("y(n)=", y)
print("x1(n)=", zx1); print("x2(n)=", zx2); print("n=", n)
plt.figure(2)
plt.subplot(3,1,1); plt.stem(n,zx1, "blue"); plt.grid()
plt.ylabel("x1(zx1)"); plt.title("Signal Multiplication")
plt.subplot(3,1,2); plt.stem(n,zx2, "blue"); plt.grid(); plt.ylabel("x2(zx2)");
plt.subplot(3,1,3); plt.stem(n,y, "blue"); plt.grid(); 
plt.xlabel("n"); plt.ylabel("y1=x1*x2")

# 5. folding
n=np.arange(min(min(nx), min(ny)), max(max(nx), max(ny))+1)
N=int(max(max(nx),max(ny))-min(min(nx), min(ny))+1)
zx=np.zeros(N); zx[int(min(nx)+abs(max(nx))) : int(max(nx)+abs(max(nx))+1)] = x
zy=np.zeros(N); zy[int(min(ny)+abs(min(ny))) : int(max(ny)+abs(min(ny))+1)] = y
plt.figure(3)
plt.subplot(2,1,1); plt.stem(n,zx, "blue"); plt.grid()
plt.ylabel("x(n)"); plt.title("Signal Folding")
plt.subplot(2,1,2); plt.stem(n,zy, "blue"); plt.grid();
plt.xlabel("n"); plt.ylabel("y(n)=x(-n)")