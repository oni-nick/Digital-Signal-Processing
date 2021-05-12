# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:51:09 2021

@author: nicholas
"""
import matplotlib.pyplot as plt
import numpy as np
from seq_module import *

n = [-3, -2, -1, 0, 1, 2, 3, 4]
xn = [2, 1, -1, 0, 1, 4, 3, 7]
plt.figure(1)
plt.stem(n, xn, "blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("x(n)")
plt.title("Representation of a sequence of x(n)") 

n0=0; n1=0; n2=20
N=n2-n1+1; n=np.arange(N)
xn = impseq(n0, n1, n2); print("Unit sample sequence=" , xn)
plt.figure(2)
plt.stem(n, xn, "blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("x(n)")
plt.title("Unit sample sequence") 

n0=0; n1=0; n2=20
N=n2-n1+1; n=np.arange(N)
xn = stepseq(n0, n1, n2); print("Unit sample sequence=" , xn)
plt.figure(3)
plt.stem(n, xn, "blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("x(n)")
plt.title("Unit step sequence") 

a=0.7
N=20; n=np.arange(N)  # 0부터 N까지 배열 생성, like range()
xn = np.power(a, n); print("Real Value exponetial=", xn)
plt.figure(4)
plt.stem(n, xn, "blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("x(n)")
plt.title("Real Value exponetial sequence") 

sigma=2; freq=3
n=np.linspace(0,10,100)  # 0~10 까지 100개로 일정하게 쪼갬.
xn=np.exp((sigma+freq*1j)*n) # 파이썬 내장 복소수 j
magxn=abs(xn)
plt.figure(5)
plt.subplot(2,1,1)
plt.stem(n, xn, "blue"); plt.grid()
plt.ylabel("x(n), Amplitude")
plt.title("Complex valued exponential sequence") 
plt.subplot(2,1,2)
plt.stem(n, magxn, "blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("|x(n)|, Magnitude")

n=np.linspace(0, 10*np.pi, 100)
xn=3*np.cos(0.1*np.pi*n+np.pi/2)
plt.figure(6)
plt.stem(n, xn, "blue"); plt.grid()
plt.xlabel("n [samples]"); plt.ylabel("Amplitude")
plt.title("Sinusoids sequence") 

xn=np.random.rand(20); print("Random Sequence")
plt.figure(7)
n=np.arange(20)
plt.stem(n, xn, "blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("Amplitude")
plt.title("Random sequence")     

x = [1,2,3,4,5,6,7]; print("x=", x)
xn=5*x; print("xn=", xn)
plt.figure(8)
n=np.arange(35)
plt.stem(n, xn, "blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("amplitude")
plt.title("Periodic sequence")        
               

