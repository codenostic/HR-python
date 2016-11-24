# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:59:29 2016

@author: bhupeshgupta
"""

'''
namedtuple - https://docs.python.org/3.5/library/collections.html#collections.namedtuple
'''

from collections import namedtuple

N = int(input())
#A, B, C, D = input().split()
student = namedtuple('student', input().split())
student_list = []
for x in range(N):
    A,B,C,D = input().split()
    student_list.append(student(A,B,C,D))
print(student_list)
total_marks = 0
for i in range(N):
    total_marks += int(student_list[i].MARKS)
print(round(total_marks/N , 2))

'''
comment - 
I got a bit stuck on creating the namedtuple. here is a super short implementation
from collections import namedtuple
N = int(input());student = namedtuple('student',input().strip().split())
print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)

But i dont know why input().split() did not work for me while creating the tuple. 
Now its working :) any ways I have used a longer approach of making a list but this is quiet short. 
I still need to work in the python way of writing sexy code. 
'''