# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:37:32 2016

@author: bhupeshgupta
"""

'''
start and end. Given a string S Print (start,end) for k in S. 
'''
import re
S = input()
k = input()
find_list = list(re.finditer(r'(?=('+k+'))', S,))
if len(find_list) != 0: 
    for found in find_list:
        print((found.start(), found.end() + len(k) -1))
else: 
    print((-1,-1))
    
'''
this solution looks optimal no changes. 
Learnt about 
1) making input to regex by putting +input+
2) look ahead
3) finditer objects 

'''