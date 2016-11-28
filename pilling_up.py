# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:46:05 2016

@author: bhupeshgupta
"""

'''
pilling up
given N cubes you need to pile up the biggest cube at bottom to smallest on top.
If you can do it - Print Yes else print No 
Inputs 
T = number of test cases 
N = number of cubes length 
list of integers each represent a cube length

Test Case 
2
6
4 3 2 1 3 4
3
1 3 2

output 
Yes
No

Solution 
What i think is that if a cube length inside is of bigger value then outer ones then it is No else Yes

So what we can do is 
Approach 1
check left most and right most value lets say LM and RM 
if LM == RM then we check max(list[1:-1]) < LM and len(list) = 2 then return Yes else got for new list = list[1:-1]
if LM > RM then we check max(list[1:]) <LM and new list - list[1:]
elseif RM > LM then we check max(list[:-1]) < RM and new list = list[:-1]
 check this recursively and if true then print yes else no
'''

#def pileup_possible(L):
#    '''
#    pileup_possible is a function that if vertical pileup of cubes is possible. 
#    bascially checks that leftmost or rightmost integers are highest then any one inside the list
#    Input - list of numbers 
#    output - True of False 
#    '''
#    
#    if len(L) == 1:
#        return True
#    elif len(L) == 2:
#        return True
#    if len(L) == 3 and (L[1] > L[0] or L[1] > L[2]):
#        return False
#    else: 
#        return True
#    if L[0] == L[-1]:
#        if (max(L[1:-1]) < L[0]):
#            pileup_possible(L[1:-1])
#        else:
#            return False
#    elif L[0] > L[-1]:
#        if max(L[1:]) < L[0]:
#            pileup_possible(L[1:])
#        else:
#            return False
#    elif L[0] < L[-1]:
#        if max(L[:-1]) < L:
#            pileup_possible(L[:-1])
#        else:
#            return False

def pileup_possible(L):
    '''
    input - list L
    check if pileup possible 
    '''
    if len(L) == 1:
        return True
    elif len(L) == 2:
        return True
    elif len(L) == 3 and (L[1] > L[0] and L[1] > L[2]):
        return False
    else: 
        for i in range(1,len(L)-1):
            if L[i] > L[i+1] and L[i] > L[i-1]:
                return False
            else: 
                return True
        
# main starts here 
T = int(input()) # number of test cases 
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    if pileup_possible(L):
        print('Yes')
    else: 
        print('No')
        
        