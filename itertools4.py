# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:44:57 2016

@author: bhupeshgupta
"""

'''
objective - basically practice permutation combintation 
Problem statement - We have a list of N lowercase letters like a, b, c... and given int K 
Need to find probability of 'a' occuring in all possible combinations of length K

'''
## getting the inputs N. S and K 
N = int(input())
S = input().split()
K = int(input())
# now i need to find all the combimations and which has 'a'
import itertools 
combin = itertools.combinations

iterator = combin(S, K)
iterations = 0 
iteration_with_a = 0

for iter_element in list(iterator):
    iterations += 1
    if 'a' in iter_element:
        iteration_with_a += 1

print(round(iteration_with_a/iterations, 4))


'''
comments 
Mine is almost fine just see a bit of changes which make teh code cleaner 
from itertools import combinations 

N = int(input())
S = raw_input().split(' ')
K = int(input())

num = 0
den = 0

for c in combinations(S,K):
    den+=1
    num+='a' in c
    
print float(num)/den

i could directly do in combinations - OK got it 

'''