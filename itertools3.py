# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:10:23 2016

@author: bhupeshgupta
"""
import itertools 
S = input()
iterator = itertools.groupby(S)
key, score = iterator.__next__()
try: 
    while key:
        iter_score = 0 
        try:
        
            while score.__next__():
                iter_score += 1
        except:        
            print((iter_score,int(key)), end = " ")
            key , score = iterator.__next__()
except:
    print()

'''
comments - this works fine but is quiet cumbersome. 
Atleast i got some idea about groupby method. looks pretty useful for grouping data
easier implementation below 
learnt that we can change object - itertools._grouper to list <- cool 

'''

# solution 2 - by editor of problem 

#for i, j in itertools.groupby(S):
#    print(tuple((len(list(j)), int(i))), end = " ")
#print()