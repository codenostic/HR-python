# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:34:19 2016

@author: bhupeshgupta
"""

'''
validate Unique ID 
rules to follow
1) atleast 2 UpperCase English characters
2) atleast 3 digits
3) only alphanumeric characters (a-z,A_Z,0-9)
4) No repeat
5) exactly 10 char in UID

'''
 

def valid_UID(test):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    
    test_upper = test
    for letter in test_upper:
        if letter not in uppercase:
            test_upper = test_upper.replace(letter, "")
    if len(test_upper) < 2:
        return False
    
    test_digit = test 
    for letter in test_digit:
        if letter not in digits:
            test_digit = test_digit.replace(letter, "")
    if len(test_digit) < 3:
        return False
        
    while test:
        letter = test[0]
        if letter not in lowercase + uppercase + digits:
            return False
        if letter in test[1:]:
            return False
        test = test[1:]
    # regex 
    return True
 

# main funcion starts here 
T = int(input())
for _ in range(T):
    test = input()
    if valid_UID(test):
        print('Valid')
    else:
        print('Invalid')


