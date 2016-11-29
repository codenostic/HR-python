# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:37:58 2016

@author: bhupeshgupta
"""

'''
timedelta - find timedifference between 2 timestamps 

'''
import datetime 

T = int(input()) # number of test cases 
for _ in range(T):
    date1 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    delta_time = date1 - date2
    print(abs(int(delta_time.total_seconds())))


'''
learnt datetime, date and time modules. 
Interesting modules but much to learn in them. 

'''