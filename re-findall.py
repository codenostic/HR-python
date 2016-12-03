# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:30:50 2016

@author: bhupeshgupta
"""

import re 
find_list = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input(), re.I)
if find_list:    
    for i in find_list:
        print(i)
else: 
    print(-1)
    
    
'''
mine is sexier but still i liked problem setters code. It is more understandable. 

he has used (lookbehind)(pattern)(lookahead)
also he has concatenated regex using '+regex+' interesting 
 
import re
consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',raw_input(),flags = re.I)
if match:
    for i in match:
        print i
else:
    print -1
    
'''