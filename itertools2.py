# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:58:25 2016

@author: bhupeshgupta
"""

S, K = input().split()
K = int(K)
import itertools
seq = itertools.permutations(S,K)
list_seq = [''.join(x) for x in seq]
list_seq.sort()
for element in list_seq:
    print(element)