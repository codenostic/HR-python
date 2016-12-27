# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:30:57 2016

@author: bhupeshgupta
"""

'''
validate Credit Card 
1) it must start 4,5 or 6 
2) 16 digits only
3) only 0-9
4) may have one '-'
5) no other separator like " " or "_"
6) no 4 consecutive same

'''
import re

def valid_card(test):
    '''
    Input - string test 
    Output - True is test is a valid credit card number format or False if Invalid
    '''
    # check 1 - string length = 16 
    # starting 4, 5 or 6 regex = [456]
    # only 0-9 or may have - regex = ([0-9]{15}|[0-9]{3}\-[0-9]{4}\-[0-9]{4}-[0-9]{4})
    # no 4 consecutive same regex  = .*(.)\1\1\1.*
    test_sub = re.sub(r'\-', "", test)
    if not re.match(r'^[456]([0-9]{15}|[0-9]{3}\-[0-9]{4}\-[0-9]{4}-[0-9]{4})$', test):
        return False
    elif re.search(r'.*(.)\1\1\1.*', test_sub):
        return False
    else:
        return True
        
    

# main function and inputs 
T = int(input()) # T = number of test Cases 
for _ in range(T):
    test = input()
    print( 'Valid' if valid_card(test) else 'Invalid')
    
'''
editor solution pretty similar 
import re
for i in range(int(raw_input())):
    S = raw_input().strip()
    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',S)
    if pre_match:
        processed_string = "".join(pre_match.group(0).split('-'))
        final_match = re.search(r'(\d)\1{3,}',processed_string)
        print 'Invalid' if final_match else 'Valid'
    else:
        print 'Invalid'
'''