# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:06:30 2016

@author: bhupeshgupta
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:08:31 2016

@author: bhupeshgupta
"""

'''
Third Try for Validating roman numberals
In solution 1 we did - 1) check basic validaions i.e.1(  max length 15, 2) only MDCLXVI,
3) M,C,X,I <4 and D, L, V < 2 then we tried to convert roman to decimal to check for error.

We can improve solution by
Approach 1
1) Check for only MDCLXVI
2) check roman valid using string operation rather than converting to decimal

what all we need to check for that. We will go from Left to right .
to be valid roman numeral form 1 to 3999 we need to check
1) M, C, X < 4 unless for special case, I < 4 for sure and D, L, V < 2
2) for S[0] = Char,  S[1] valid or not
'''
import re 

def validate_roman(S):
    is_roman = True 
    is_roman =  False if (re.match(r'(?![MDCLXVI])', S)) else True    
    if is_roman:
        is_roman = False if ((re.search(r'((?<=[LDXVI])(M))', S)) or \
        (re.search(r'((?<=[LVI])(C))', S)) or (re.search(r'((?<=[LXVI])(D))', S)) or \
        (re.search(r'((?<=[V])(X))', S)) or re.search(r'((?<=[VI])(L))', S)) else True  

#    if ((S.count('M') > 3) and ('MMMCM' not in S)) or \
#    ((S.rfind('M') > 0) and (S[S.rfind('M')-1] in 'LDXVI')):
#        is_roman = False
#    elif ((S.count('C') > 3) and ('CCCXC' not in S)) or \
#    ((S.rfind('C') > 0) and (S[S.rfind('C')-1] in 'LVI')):
#        is_roman = False
#    elif ((S.count('D') > 1)) or \
#    ((S.rfind('D') > 0) and (S[S.rfind('D')-1] in 'LXVI')) :
#        is_roman = False
#    elif ((S.count('X') > 3) and ('XXXIX' not in S)) or \
#    ((S.rfind('X') > 0) and (S[S.rfind('X')-1] in 'V')):
#        is_roman = False
#    elif ((S.count('L') > 1)) or \
#    ((S.rfind('L') > 0) and (S[S.rfind('L')-1] in 'VI')):
#        is_roman = False
#    elif ((S.count('I') >3)):
#        is_roman = False
#    elif (S.count('V') > 1):
#        is_roman = False
    return is_roman

S = input()
print(validate_roman(S))
