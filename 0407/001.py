# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:40:24 2021

@author: nicholas
"""
import numpy as np
import matplotlib.pylab as plt

n = [-3, -2, -1, 0, 1, 2, 3, 4]
xn = [2, 1, -1, 0, 1, 4, 3, 7]
plt.figure()
plt.stem(n, xn, "blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("x(n)")
plt.title("Representation of a sequence of x(n)") 