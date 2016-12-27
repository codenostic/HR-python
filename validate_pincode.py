# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:21:34 2016

@author: bhupeshgupta
"""

'''
valid postal code 
1) numbers between 100000 - 999999
2) max 1 alternating repeating digit

'''

# between 100000 - 999999 ^[1-9][0-9]{5}$

import re 
test = input()
print(bool(re.match(r'^[1-9][0-9]{5}$', test)) and (len(re.findall(r'(.)(?=[0-9]\1)', test)) < 2))

'''
exactly same solution as editor 
import re
P = raw_input()
print len(re.findall(r'(?=(\d)\d\1)',P)) < 2 and bool(re.match(r'^[1-9][0-9]{5}$',P))
'''