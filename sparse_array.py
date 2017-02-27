# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:58:49 2017

@author: bhupeshgupta
"""

'''
sparse Array
Given N strings and Q queries you need to search how many time teh string occured previously

'''

# main function starts here 
if __name__ == "__main__":
    N = int(input())
    strings_list = []
    for _ in range(N):
        strings_list.append(input())
    Q = int(input())
    for _ in range(Q):
        print(strings_list.count(input()))

'''
this is quiet neat implementation 
'''