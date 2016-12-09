# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:08:31 2016

@author: bhupeshgupta
"""

'''
Second Try for Validating roman numberals
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

def validate_roman(S):
    for letter in S:
        if letter not in "MDCLXVI":
            return False

    d_s = S
    while d_s:
        if d_s[0] == "M":
            if (d_s.count('M') > 3) and ('MMMCM' not in d_s):
                return False
            elif (d_s.rfind('M') > 0) and (d_s[d_s.rfind('M')-1] in 'LDXVI'):
                return False
            else:
                d_s = d_s.replace('M', "")
        elif d_s[0] == "C":
            if (d_s.count('C') > 3) and ('CCCXC' not in d_s):
                return False
            elif (d_s.rfind('C') > 0) and (d_s[d_s.rfind('C')-1] in 'LVI'):
                return False
            else:
                d_s = d_s.replace('C', "")
        elif d_s[0] == 'D':
            if (d_s.count('D') > 1):
                return False
            elif (d_s.rfind('D') > 0) and (d_s[d_s.rfind('D')-1] in 'LXVI'):
                return False
            else:
                d_s = d_s.replace('D', "")
        elif d_s[0] == 'X':
            if (d_s.count('X') > 3) and ('XXXIX' not in d_s):
                return False
            elif (d_s.rfind('X') > 0) and (d_s[d_s.rfind('X')-1] in 'V'):
                return False
            else:
                d_s = d_s.replace('X', "")
        elif d_s[0] == 'L':
            if (d_s.count('L') > 1):
                return False
            elif (d_s.rfind('L') > 0) and (d_s[d_s.rfind('L')-1] in 'VI'):
                return False
            else:
                d_s = d_s.replace('L', "")
        elif d_s[0] == 'I':
            if (d_s.count('I') >3):
                return False
            else:
                d_s = d_s.replace('I', "")
        elif d_s[0] == 'V':
            if (d_s.count('V') > 1):
                return False
            else:
                d_s = d_s.replace('V', "")
    return True

S = input()
print(validate_roman(S))
