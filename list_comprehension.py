# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 12:05:54 2016

@author: bhupeshgupta
"""

A = int(input())
B = int(input())
C = int(input())
N = int(input())

list = [[a,b,c] for a in range(A+1) for b in range(B+1) for c in range(C+1) if a+b+c !=N]
list.sort()
print(list)