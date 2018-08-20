# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 09:00:04 2018

@author: CSE
"""

#program to print the sqrare root of a number

def sqrt(x):
    g = x/2.0
    while True:
        a = (g+x/g)/2
        if abs(a-g)<0.01:
            return a
        g = a
        
print(sqrt(9))         