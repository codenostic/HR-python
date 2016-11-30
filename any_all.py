# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:39:29 2016

@author: bhupeshgupta
"""

'''
any or all - built-infunctions forcheck - https://docs.python.org/2/library/functions.html

given a list of integers check if any one is palindrome or not

'''

# getting inputs 
N = int(input())
int_list = list(map(int, input().split())) # list of numbers to be checked is any of them is iterable
print(any(map(lambda x : str(x) == str(x)[::-1], int_list)))
