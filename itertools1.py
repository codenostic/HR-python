# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:35:34 2016

@author: bhupeshgupta
"""

import itertools
A = [x for x in map(int, input().split())]
B = [x for x in map(int, input().split())]
X = itertools.product(A, B)
for _ in X:
    print(_ , end = " ")
print()