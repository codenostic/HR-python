# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:44:51 2016

@author: bhupeshgupta
"""

'''
solution 1 
1) make nested list of [name, marks]
2) sort by marks
3) find second highest marks
4) make a list of names with second highest marks
5) sort the list of names 
6) display each name 

solution 2 - dictionary 
1) make a dictionary {name:marks}
2) sort dictionary using sorted(x.items(), key=operator.itemgetter(1)) (import operator)
3) make list of names with second highest values 
4) sort and print 

solution 3 
1) nested list [name, marks]
2) find the second highest marks and make a list of names associated with them
3) sort and print



'''

N = int(input())
students = []
for _ in range(N):
    name = input()
    marks = float(input())
    students.append([ name, marks ])


# sort the list as per grades
names_2ndhighest = [students[0][0]]     #initialize to first name
lowest_marks , lowest_name = students[0][1], students[0][0]              #initialize to marks of first student
secondlowest_marks, secondlowest_name = students[0][1], students[0][0]       #initialize to makrs of first student
for i in range(1,N):
    if students[i][1] < lowest_marks and lowest_marks == secondlowest_marks:
        lowest_marks = students[i][1]
    elif students[i][1] < lowest_marks and lowest_marks != secondlowest_marks:
        secondlowest_marks, secondlowest_name = lowest_marks, lowest_name
        lowest_marks, lowest_name = students[i][1], students[i][0]
        names_2ndhighest.clear()
        names_2ndhighest.append(secondlowest_name)
    elif students[i][1] > lowest_marks and lowest_marks == secondlowest_marks:
        secondlowest_marks, secondlowest_name = students[i][1], students[i][0]
        names_2ndhighest.clear()
        names_2ndhighest.append(secondlowest_name)        
    elif students[i][1] > lowest_marks and students[i][1] < secondlowest_marks:
        secondlowest_marks, secondlowest_name = students[i][1], students[i][0]
        names_2ndhighest.clear()
        names_2ndhighest.append(secondlowest_name)
    elif students[i][1] == secondlowest_marks:
        names_2ndhighest.append(students[i][0])

names_2ndhighest.sort()
for name in names_2ndhighest:
    print(name)
