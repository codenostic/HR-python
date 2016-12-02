# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:01:35 2016

@author: bhupeshgupta
"""

'''
re.split() function to be used 

'''

import re 

pattern = re.compile('[,\.]')
splitall = re.split(pattern, input())

for i in splitall:
    if i !='':
        print(i)
        
'''
looks like inside [] we dont need to put \ for . Hmmm..... interesting 
'''