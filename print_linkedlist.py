# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:32:10 2017

@author: bhupeshgupta
"""

"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 
"""

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data 
        self.next = next_node
    


def print_list(head):
    if head is None:
        exit 
    else: 
        print(head.data)
        head = head.next
        print_list(head)

'''
neat and concise implementation. 
'''