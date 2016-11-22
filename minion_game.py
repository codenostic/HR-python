# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:16:47 2016

@author: bhupeshgupta
"""

'''
Objective of Game:
Given String S - 2 players make Substrings starting with consonants and vowels.  
Which ever has more number of substring wins. 

Test Case 
S = BANANA (Input)
Stuart (Makes COnsonant) = B, N , BA, NA, BAN, NAN, BANA, NANA, BANAN, BANANA = Total substring = 12
KEVIN (Makes Vowels) = A, AN, ANA, ANAN, ANANA - Substrings = 9 
(Output) - Staurt 12 

Solution 1 - 

We need to make substrings and then bucket them under stuart and kevin and see who has more. 
steps 
1) Make a list of substrings = len 1 to len(S)
2) If substring starts with vowel then Kevin_score +1 else Stuart_score +1 
3) print score 

Key thing - how to make a list of substrings of size 1 to len(S)
for length in range 1 to len(S) + 1
    for index in range(len(S) - length + 1)
        substring = S[index:index+length]
        substring_list.append(substring)
        
Solution 2 - 
    for index in range (len(S))
        if S[index] == Vowel
            then Kevin score = len(S) - index + 1
        else:
            stuart_score = len(S) - index + 1
            
'''

S = input()
#print(substrings(S))
stuart_score = 0
kevin_score = 0
for index in range(len(S)):
        if S[index] in "AEIOU":
            kevin_score += len(S) - index
        else:
            stuart_score += len(S) - index 

if stuart_score > kevin_score:
    print("Stuart", str(stuart_score))
elif kevin_score > stuart_score:
    print("Kevin", str(kevin_score))
else:
    print("Draw")
