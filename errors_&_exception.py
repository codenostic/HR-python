# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:15:35 2016

@author: bhupeshgupta
"""

'''
errors and exceptions
'''

T = int(input())
for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as err: 
        print('Error Code: {0}'.format(err))


'''
Learnt using format. error and exception looks useful now. 
'''