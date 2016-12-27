# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:26:10 2016

@author: bhupeshgupta
"""
import re

def valid_UID(test):
    if len(re.findall(r'[A-Z]', test)) < 2:
        return False
    elif len(re.findall(r'[0-9]', test)) < 3:
        return False
    elif not bool(re.search(r'[a-zA-Z0-9]{10}', test)):
        return False
    elif re.search(r'.*(.).*\1', test):
        return False
    else:
        return True

# main funcion starts here 
T = int(input())
for _ in range(T):
    test = input()
    if valid_UID(test):
        print('Valid')
    else:
        print('Invalid')
        
'''
problem setters code is pretty similar to what we have done here. but check

import re
for i in range(int(raw_input())):
    N = raw_input().strip()
    if N.isalnum() and len(N) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}',N)) and bool(re.search(r'(.*[0-9]){3,}',N)):
            if re.search(r'.*(.).*\1+.*',N):
                print 'Invalid'
            else:
                print 'Valid'    
        else:
            print 'Invalid'
    else:
        print 'Invalid'
'''