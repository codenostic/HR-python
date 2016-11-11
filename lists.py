# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:30:12 2016

@author: bhupeshgupta
"""

list = []
n = int(input())
for _ in range(n):
    command = input()
    if 'insert' in command:
        insert_command, index, insert_value = command.split()
        list.insert(int(index), int(insert_value))
    elif 'print' in command:
        print(list)
    elif 'remove' in command:
        rem_comm, remove_value = command.split()
        list.remove(int(remove_value))
    elif 'append' in command:
        app_comm, append_value = command.split()
        list.append(int(append_value))
    elif 'sort' in command:
        list.sort()
    elif 'pop' in command:
        list.pop()
    elif 'reverse' in command:
        list.reverse()