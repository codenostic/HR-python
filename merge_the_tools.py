# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:17:49 2016

@author: bhupeshgupta
"""

'''
objective - Give string S of length = n, and integer k (n is multiple of k)
divide it into subsegments ti where i = 1 to n/k

for each ti find ui with non duplicate characters 

Test Case 
input 
AABCAAADA
3 

output 
AB
CA
AD

Solution 1
1) index goes from 0 to len(S) - 1 with steps of k for each index make a subsegment t of K elements 
2) for each subsegment t, make a unique_substring by \
going to each charatcter and adding in unique_substring if unique else no
3) come out of loop and print the unique_substring
'''

S = input()
K = int(input())

seg_t = ""
for index in range(0,len(S),K):
    seg_t = S[index:index+K]
    unique_string = ""
    for CR in seg_t:
        if CR not in unique_string:
            unique_string += CR
    print(unique_string)