# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:46:07 2016

@author: bhupeshgupta
"""

import re 
T = int(input())
for _ in range(T):
    s = input()
    print(bool(re.match(r'([+-]?\d*\.\d*$)', s)))
    
    
'''
this code looks good, couple of things we could change i.e. add ^infront for start 
and \d+ after period for one and more rather than using * which is for 0 and more. 
Ok great check teh editors code 

import re
for i in range(int(raw_input())):
    print bool(re.search(r"^[+-]?\d*\.\d+$",raw_input().strip()))
'''