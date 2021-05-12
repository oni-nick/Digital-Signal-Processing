# -*- coding: utf-8 -*-
"""
Created on Wed May 12 11:42:20 2021

@author: nicholas
"""

from seq_module import *
import matplotlib.pyplot as plt
import numpy as np
n = np.arange(-5,6)
xn = 2 * impseq(-2,-5,5) - impseq(4,-5,5)
plt.subplot(4,1,1); plt.stem(n, xn, "blue"); plt.grid(); plt.ylabel("A: x(n)");
 
n=np.arange(0,21)
xn1 = n * stepseq(0,0,20) - stepseq(10,0,20)
xn2 = 10 * np.exp(-0.3 * (n-10)) * (stepseq(10,0,20) - stepseq(20,0,20))
xn = xn1 + xn2
plt.subplot(4,1,2); plt.stem(n, xn, "blue"); plt.grid(); plt.ylabel("B: x(n)");

n=np.arange(0,51)
xn=np.cos(0.04*np.pi*n) + 0.2*np.random.rand(len(n))
plt.subplot(4,1,3); plt.stem(n,xn,"blue"); plt.grid(); plt.ylabel("X: x(n)")

n=np.arange(-10,10)
x=[5,4,3,2,1]
xn = 4*x
plt.subplot(4,1,4); plt.stem(x,xn,"blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("D: x(n)")
