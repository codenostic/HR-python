# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:03:09 2016

@author: bhupeshgupta
"""

'''
Most Common - Given string S, find 3 most common alphabets. 

Test Case
Input
aabbbccde

Output 
b 3
a 2
c 2

problem parts 
1) make a dictionary of letters in string with their occurence
2) 
'''
S = input()
d = {}

from itertools import groupby
from operator import itemgetter
for x in S:
    if x in d:
        d[x] +=1
    else: 
        d[x] = 1
l = sorted(d.items(), key = lambda x : (-x[1], x[0]))[:3]
print(l)
l = groupby(l, key = itemgetter(1))
tuple_list_items = []
for key, items in l:
    items_list = list(items)
    items_list.sort()
    for item in items_list:   
        tuple_list_items.append(item)

tuple_list_items = tuple_list_items[:3]
for char, value in tuple_list_items:
    print(char, value)

# clumsy solution 1
#item_number = 0
#for key, items in l:
#    item_list = list(items)
#    item_list.sort()
#    if item_number >= 3:
#        break
#    for item in item_list:
#        print(item[0], key)
#        item_number += 1
##        print(item_number)
#        if item_number >= 3:
#            break


#'''
#solved the problem but this is the most clumsy code i have writen ever. Lets improve it now 
#Clumsiness 
#1) max clumsy thing i did - using 2 if statements and using break statements :P 
#2) make dict, then sort, then groupby, then print - can we do it in lesser steps. hmmmmmm 
#lets first deal with break statements 
#the second one looks a bit less clumsy as it has no stupid breaks . lets keep that for now 
#
#Interesting thing i noticed is that in groupby the item has the whole item. 
#so its better to sort the list by the key you want to groupby. and then use groupby. 
#also, in general if you sort a list of tuples it will sort using the item at index = 0 
#
#
#shit man i should have read the collections and used Counter - Fucking shit simple it is. 
#Aweosme solution look below
# All three are great ways to do it 
# 
# Approach:
#
#STEP 1: Create a list, letters, of size . Initialize each element to .
#
#STEP 2: Traverse through the input string . If a character in the string is 'a', then increment letter by . If 'b' is found, then increment letter by  and so on.
#
#STEP 3: Now run a loop three times. Inside the loop, store the maximum value of letters in the variable max_letter.
#
#STEP 4:. In the scope of the previous loop, run another loop and find the index of the first occurrence of max_letter. Now, print the appropriate letter associated with that index and the max_letter.
# Set by DOSHI
#
#Problem Setter's code :
#SOLUTION 1 --
#
#S = raw_input()
#letters = [0]*26
#
#for letter in S:
#    letters[ord(letter)-ord('a')] += 1
#
#for _ in range(3):
#    
#    max_letter = max(letters)
#    
#    for index in range(26):
#        if max_letter == letters[index]:
#            print chr(ord('a')+index), max_letter
#            letters[index] = -1
#            break
#
#
#Counter Solution 1
#
#from collections import Counter
#from operator import itemgetter
#
#for item in (sorted(sorted(Counter(raw_input()).items()), key = itemgetter(1), reverse = True)[:3]):
#    print item[0], item[1]
#
#
#The best solution 
#
#Counter Solution 2
#from collections import Counter
#
#for letter, counts in sorted(Counter(raw_input()).most_common(),key = lambda x:(-x[1],x[0]))[:3]:
#    print letter, counts
# awesoem use of lambda,  counter  and - sign for reverse sorting never know this 
#- learnt alot for one day. Awesome. 
#
#'''