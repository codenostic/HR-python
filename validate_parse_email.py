# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:52:48 2016

@author: bhupeshgupta
"""

'''
Validate and Parse email Address 
Input - Interger N and then N lines of name <email> 
Output - Print name <email> for valid email address 

'''
import email.utils
import re


#Input and main function 
N = int(input())
for _ in range(N):
    S = input()
    name, email_id = email.utils.parseaddr(S)   #parse name, email id 
    if re.match(r'^[a-zA-Z][a-zA-Z0-9-_\.]+@[a-z]+\.[a-z]{1,3}$', email_id):
        print(S)                                # print S if email-id Valid use regex 
        

'''
Answer is correct but a new thins quantifiers 1 and 3 noth included so no need to do 4
'''