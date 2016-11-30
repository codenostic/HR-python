# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:14:20 2016

@author: bhupeshgupta
"""

N, M = map(int, input().split())
data_list = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
data_list.sort(key = lambda x : x[K])
for X in data_list:
    print(" ".join(str(x) for x in X))
