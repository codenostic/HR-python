# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 12:36:16 2016

@author: bhupeshgupta
"""

N = int(input())
a_list = [x for x in map(int,input().split())]
a_list.sort()

max1 = a_list[0]
max2 = a_list[0]
for i in range(N):
    if a_list[i] > max1:
        max2 = max1
        max1 = a_list[i]
print(max2)