# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:39:39 2016

@author: bhupeshgupta
"""
import itertools
K, M = map(int, input().split())

arrayN = [list(map(int, input().split()[1:])) for _ in range(K)]
possible_combinations = list(itertools.product(*arrayN))

def func(nums):
    return sum(x*x for x in nums)%M

# main function 
print(max(list(map(func, possible_combinations))))


'''
nice question and great implementation. here is another way to do it. looks neat
check out the usage of *argument this is very useful
*argument is the way to pass multiple arguments in a function. 

from itertools import *

K, M = map(int, raw_input().split())
N = []

for _ in xrange(K):
     N.append(map(int, raw_input().split())[1:])        
MAX = -1
for i in product(*N):
    MAX = max(sum(map(lambda x: x**2, i))%M, MAX)
    
print MAX  
'''