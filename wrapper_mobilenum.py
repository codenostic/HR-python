# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 16:16:34 2017

@author: bhupeshgupta
"""

'''
wrapper for mobile numbers 

'''
def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            if len(l[i]) == 10:
                l[i] = '+91 ' + l[i][:5] + ' ' + l[i][5:]
            if len(l[i]) == 11:
                l[i] = '+91 ' + l[i][1:6] + ' ' + l[i][6:]
            if len(l[i]) == 12:
                l[i] = '+91 ' + l[i][2:7] + ' ' + l[i][7:]
            if len(l[i]) == 13:
                l[i] = '+91 ' + l[i][3:8] + ' ' + l[i][8:]
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep = '\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
