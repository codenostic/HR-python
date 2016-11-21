# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:07:46 2016

@author: bhupeshgupta
"""

'''
Objective - Give a string S - Swap Case of each alphabet. 

Examples/Test Cases  
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

solution 1
Make 2 strings of lowercase and upperCASE 
if alphabet in lowercase - insert corresponding UpperCase \
else if in UPPERCASE then insert lowercase in a new string 

Solution 2 
make a string of LOWER+UPPER and newindex = index + 26 if index <= 25 
else index + 26 - 52 if index > 52

'''

S = input()
eng_alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
newS = ""
for letter in S:
    if letter not in eng_alphabets:
        newS = newS + letter 
    elif letter in eng_alphabets and eng_alphabets.index(letter) <= 25:
        newS = newS + eng_alphabets[eng_alphabets.index(letter) + 26]
    elif letter in eng_alphabets and eng_alphabets.index(letter) > 25:
        newS = newS + eng_alphabets[eng_alphabets.index(letter) + 26 -52]

print(newS)
