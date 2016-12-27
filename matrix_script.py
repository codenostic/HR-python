# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:47:41 2016

@author: bhupeshgupta
"""


'''
Decode matrix 
given NXM matrix followed by N strings or M characters. 
output - decodes string 
'''
import re 

#main function
N, M = map(int, input().split())
#print(N, M) # prinyt statement for debugging 
matrix = []
for _ in range(N):
    string_list = list(input())
#    print(string_list)
    matrix.append(string_list)
#print(matrix)

script = ''
for i in range(M):
    for j in range(N):
        script += matrix[j][i]

#print(script)

print(re.sub(r'(?<=[a-zA-z0-9])[!@#$%&\s]+(?=[a-zA-Z0-9])', " ", script))

'''
editor has done the same thing just used a clever way or reducing code to one line 
check out 
import re
matrix = []
N,M = map(int, raw_input().split())
for i in range(N):
    matrix.append(list(raw_input()))
print re.sub(r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])',' ',"".join("".join(decode) for decode in zip(*matrix)))

I am not really impressed. I guess my solution is more readable and understandable even if longer. 
'''