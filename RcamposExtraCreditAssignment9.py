# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:13:47 2022

@author: ronal
"""

def gcd(x,y): return y and gcd(y, x % y) or x
def lcm(x,y): return x * y / gcd(x,y)

n = 1
for i in range(1, 31):
     n = lcm(n, i)
print(n)