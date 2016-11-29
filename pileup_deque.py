# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:07:04 2016

@author: bhupeshgupta
"""

'''
SOlving Pile up using deque

'''

from collections import deque

# main function here 
T = int(input()) # number of test cases 
for _ in range(T):
    
    N = int(input()) # number of integers in list 
    int_list = deque(map(int, input().split()))
    top_cube = 0
    while int_list:
        if top_cube == 0:
            top_cube = max(int_list[0], int_list[-1])
            if int_list[0] >= int_list[-1]:
                int_list.popleft()
            else:
                int_list.pop()
        elif top_cube >= max(int_list[0], int_list[-1]):
            top_cube = max(int_list[0], int_list[-1])
            if int_list[0] >= int_list[-1]:
                int_list.popleft()
            else:
                int_list.pop()
        else: 
            break
    print('Yes') if len(int_list) == 0 else print('No')

'''
Yo!!! Got it with deque also. This look much more cleaner code. 
'''