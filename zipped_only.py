# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:08:21 2016

@author: bhupeshgupta
"""

def zipped(*args):
    zip_lists = [list(a) for a in args]
    result = []
    for i in range(len(zip_lists[0])):
        temp_list = []
        for x in zip_lists:
            temp_list = temp_list +[x[i]]
        result = result + [temp_list]
    return result



A = [1,2,3]
B = [4,5,6]
C = [7,8,9]
args = [A] + [B] + [C]

print(zipped(*args))