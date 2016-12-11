# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:34:19 2016

@author: bhupeshgupta
"""

'''
validate Unique ID 
rules to follow
1) atleast 2 UpperCase English characters
2) atleast 3 digits
3) only alphanumeric characters (a-z,A_Z,0-9)
4) No repeat
5) exactly 10 char in UID

'''

import re 

T = int(input())
for _ in range(T):
    test = input()
    if re.match(r'testpattern', test):
        print('Valid')
    else:
        print('Invalid')


