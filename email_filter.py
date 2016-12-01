# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 12:03:40 2016

@author: bhupeshgupta
"""

'''
using filter function 

Testcase 
Input 
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Output 
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

for valid email what we do is that 
1) till @ we should check each element is under username, after that till . it should be in webname
 and after that len <=3
 
'''
def valid_email(S):
    valid_username_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
    valid_websitename_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ0123456789'
    if '@' not in S:
        return False
    elif '.' not in S:
        return False 

    username = ''
    websitename = ''
    extensionname = ''
    
    while S[0] != '@':
        username += S[0]
        S = S[1:]
    
    S = S[1:]
    
    while S[0] != '.':
        websitename += S[0]
        S = S[1:]
    
    S = S[1:]
    
    extensionname = S[:]
    
    for u in username:
        if u not in valid_username_letters:
            return False
    for w in websitename:
        if w not in valid_websitename_letters:
            return False
    
    if len(extensionname) > 3 or len(username) ==0 or len(websitename) == 0 :
        return False
    
    return True


N = int(input())
name_list = []
for _ in range(N):
    name_list.append(input())
name_list = list(filter(valid_email, name_list))
name_list.sort()
print(list(name_list))



'''
used regex to solve it. which is good and i know that email validation is done using regex
Need to learn regex. Solution below 

import re
lst = list()
for i in range(int(raw_input())):
    lst.append(raw_input())
print sorted(list(filter(lambda x: re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$',x),lst)))
'''