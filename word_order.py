# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 18:09:58 2016

@author: bhupeshgupta
"""

'''
word order 
You are given  words. Some words may repeat. 
For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. 

Example- 
Input
4
bcdef
abcdefg
bcde
bcdef

Output 
3
2 1 1

I guess we can use defaultdict for this 
'''
N = int(input()) ;
d = dict()
for num in range(N):
    S = input()
    if S in d:
        d[S][1] += 1
    else:
        d[S] = [num,1]

print(len(d.keys()))
for x in sorted(list(d.values())):
    print(x[1], end = ' ')
print()

'''
solved it but not very happy with the solution. lets see what the editor has done. 
oops he has used ordereddict - hmmmm .... i dod not see that great. I will remember that
easy solution 

from collections import OrderedDict

d=OrderedDict()
n=int(input())
for i in range(n):
    s=input()
    if s in d.keys():
        d[s]+=1
    else:
        d[s]=1
print(len(d.keys()))
print(' '.join([str(d[k]) for k in d.keys()]))
'''