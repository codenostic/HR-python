# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:58:58 2016

@author: bhupeshgupta
"""

'''
make builtin function zip 
zip ([iterable, ...]) -> returns a list of tuples where ith tuple contains ith element of each iterable

'''

def zipped(*args):
    '''
    given args return a list of tuples 
    Input - args 
    output - list of tuples 
    '''
    pass # remove this when you add code     



# main function Here 

num_students, marks_lists = map(int, input().split())
marks_matrix = [list(map(float, input().split())) for _ in range(marks_lists)]
for marks_sum in list(map(sum, zipped(*marks_matrix))):
    print(".1f"%(marks_sum/marks_lists))