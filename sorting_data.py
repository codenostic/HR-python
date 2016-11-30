# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:55:21 2016

@author: bhupeshgupta
"""

import functools
s = input()
list_s = sorted(s, key = lambda x : (x.isnumeric() and not (int(x))%2, x.isnumeric() and (int(x))%2,  x and x.isupper(), x))
string_s = functools.reduce(lambda x,y: x + y, list_s)
print(string_s)

'''
mine is sexier but another simple solution we could do 
from __future__ import print_function

upper = []
lower = []
even = []
odd = []

def separator(a):
    
    if a.isalpha():
        if a.isupper():
            upper.append(a)
        else:
            lower.append(a)
    else:
        if int(a)%2 == 0:
            even.append(a)
        else:
            odd.append(a)
    return 
    
map(separator,raw_input())       

upper.sort()
lower.sort()
even.sort()
odd.sort()

t = lower+upper+odd+even
map(lambda x: print(x,end=''),t)
'''