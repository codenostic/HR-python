# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:40:05 2017

@author: bhupeshgupta
"""

from collections import deque

class Node:
    def __init__(self, index):
        self.left = None
        self.right = None
        self.index = index
        
    
def in_order_traverse(root):
    """Don't use recursion b/c of recursion limit."""
    '''
    this is straight forward, basically append right then node then left in stack
    so that you open left first
    visited is clever way. 
    I liked this solution by far rhe most except 
    i did not undertsand how he used left_index and right_index without that in Class Node
    '''    
    stack = deque([root])
    visited = set()
    while stack:
        node = stack.pop()
        if node is None:
            continue # returns control to while loop and reject all statements below
        if node.index in visited:
            print(node.index, end=' ')
            continue
        visited.add(node.index)
        stack.append(node.right)
        stack.append(node)
        stack.append(node.left)
    
    
def swap(root, k):
    """Don't use recursion b/c of recursion limit."""
    q = deque([(root, 1)])
    while q:
        node, level = q.popleft()
        # if node is none then move to next node
        if node is None: 
            continue
        # if level = multiple of K -> swap else node.left and right in stack
        if level % k == 0: 
            node.left, node.right = node.right, node.left
        q.append((node.left, level+1))
        q.append((node.right, level+1))

        
        
# get number of nodes    
N = int(input())

# create node list
nodes = [None]*(N+1)
for i in range(1, N+1):
    n = Node(i)
    # this a tuple added to n but how as there is no left_index and right_index in Node
    n.left_index, n.right_index = [v if v > 0 else 0 for v in map(int, input().split())]
    # very CLever - when n.left_index and right_index = 0 so nodes[n.left_index] == None
    nodes[i] = n

# fill out node objects
for n in nodes[1:]:
    left = nodes[n.left_index] # = None when n.left_index = 0 
    right = nodes[n.right_index] # = None when n.left_index = 0 
    n.left = left # basically stores the pointer to the node 
    n.right = right # basically stores the pointer to the node

T = int(input())
root = nodes[1]
# do the swapping
for _ in range(T):
    k = int(input())
    swap(root, k)
    in_order_traverse(root)
    print('')
    
