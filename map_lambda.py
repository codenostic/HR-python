# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:27:40 2016

@author: bhupeshgupta
"""

'''
using map and lambda function

given an integer N - print a list of cubes of fibbonaci numbers 

solution - 
1) define lambda function for fibbonaci 
2) apply fibbonaci to N numbers then appy cube to them 

'''

fib = lambda x: x if x < 2 else fib(x-1) + fib(x-2)
N = int(input())
L = list(map(fib, list(range(N))))
print(list(map(lambda x: x**3, L)))