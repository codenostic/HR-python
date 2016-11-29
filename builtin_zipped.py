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
    zip_lists = [list(a) for a in args]
    result = []
    for i in range(len(zip_lists[0])):
        temp_list = []
        for x in zip_lists:
            temp_list = temp_list +[x[i]]
        result = result + [temp_list]
    return result

# main function Here 

num_students, marks_lists = map(int, input().split())
marks_matrix = [list(map(float, input().split())) for _ in range(marks_lists)]
for marks_sum in list(map(sum, zipped(*marks_matrix))):
    print(marks_sum/marks_lists)
    