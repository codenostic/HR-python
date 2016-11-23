# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:15:28 2016

@author: bhupeshgupta
"""

'''
defaultdict - Read more here - https://docs.python.org/3.5/library/collections.html#collections.defaultdict

'''
from collections import defaultdict

n, m = map(int, input().split())
dd_n = defaultdict(list)
counter = 1
for i in range(n):
    letter = input()
    dd_n[letter].append(counter)
    counter += 1
for _ in range(m) :
    find_letter = input()
    if find_letter in dd_n:
        for x in dd_n[find_letter]:
            print(x, end = ' ')
        print()
    else: 
        print(-1)