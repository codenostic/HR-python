# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:53:48 2016

@author: bhupeshgupta
"""
'''
objective - Given N, Make alphabet rangoli with alphabets ranging from A = 1 to Alphabet = N
0 < N < 27
example 
N = 3 then pattern 
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

N = 5 then pattern 
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

Solution 1: 
We can create a dictionary of strings for rows 1 to 2N-1 and then print them one by one

Solution 2: ?

'''

def rangoli_dict(N):
    '''
    Given Integer N gives back a dictionary with 2N-1 elements \
    having the required pattern for each row
    Input: Integer N 
    Output: Dictionary with pattern of each row as shown above corresponding to row number
    '''
    '''
    Pseudocode:
    for loop from row number (RN)  = 1 to (2N-1)//2 <- sub - middle row 
    we need to enter RN_pattern corresponding to RN and (2N-1) - RN +1 (both will be similar)
    After for loop we add pattern for RN = (2N-1)//2 +1 <- Middle Row
    
    What is RN_Pattern corresponding to RN 
    Note that in Rangoli we will have 4N-3 columns because 
    N alphabets on right + N-1 alphabets on left \
    + the - separators for (N+N-1) which will be (N+N-1) - 1
    Hence totally N + N-1 + (N+N-1) - 1 = 4N -3
    
    Now for each RN we will have 4RN - 3 as rn_pattern in center and rest -'s 
    hence RN_DASH = (4N-3) -(4RN-3))//2 -'s on each side 
    
    hence RN_Pattern = "-"*RN_DASH + rn_pattern + "-"*RN_Dash
    
    how do we make rn_pattern for each RN we need to make right side and left side pattern
    so lets make a string such as 'a-b-c-d-e'and reverse string such as 'e-d-c-b'ready 
    so that we can easily slice and add the slices 
    
    we should have a string of lower case alphabets which we can join using '-'
    
    so lets start     
    '''
    
    low_case_alpha = "abcdefghijklmnopqrstuvwxyz"
    straight_string_rangoli = low_case_alpha[:N] # alphabets till index N-1 
    reverse_string_rangoli = straight_string_rangoli[:0:-1] # list of alphabets in reverse - the first alphabet
    right_string = "-".join(straight_string_rangoli)
    left_string = "-".join(reverse_string_rangoli)
    rangoli = {}
    for RN in range(1,((2*N-1)//2)+1):
        if RN == 1:
            rn_pattern = left_string[:RN]
        else:
            rn_pattern = left_string[:2*(RN-1)-1] + "-" + right_string[((2*N-1) - (2*(RN)-1)):]
        
        RN_Dash = ((4*N-3) - (4*RN -3))//2
        RN_Pattern = "-"*RN_Dash + rn_pattern + "-"*RN_Dash
        rangoli[RN] = RN_Pattern
        rangoli[(2*N-1)-RN+1] = RN_Pattern
    
    if N == 1:
        rangoli[1] = right_string
    else:
        rangoli[(2*N-1)//2 + 1 ] = left_string  + "-" + right_string # middle row
    
    return rangoli


# main function starts here 

N = int(input())
dict_rangoli = rangoli_dict(N)
for key in dict_rangoli.keys():
    print(dict_rangoli[key])