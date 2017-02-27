# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 16:00:11 2017

@author: bhupeshgupta
"""
'''
Interesting Problem - Bugger does not want to do any effort. 
He wants me to first make the tree and then do the Swap Algo part also. Asshole 
Anyways lets do this. 
So what do we have to do. 
Given a Btree and K, We need to swap nodes at depth h where h belongs to [k, 2k, 3k...]

Input - 
1) First Input will be N i.e the size of Tree with nodes [1...N] root node = 1
2) Next N inputs will be integers a, b where a is left child and b is right child for ith Node
3) After that Integer T - T is number of test cases each giving value K 
4) Next T inputs each comtaining K where we need to swap

Output 
for each K do swap at K, 2k, 3k ...... and then print the tree inOrder

So what do we need for this 
1) we need a class Node_Btree which has struct data, left_node, right_Node 
2) Methods - Insert_node, Depth, print_inOrder, Swap_depth(), 
3) next we will have main function that reads the input and implements the Solution 

Sure, lets put this down in a structure and see if this is sufficient for getting things done. 
'''
#import time
#
#def timing(f):
#    def wrap(*args):
#        time1 = time.time()
#        ret = f(*args)
#        time2 = time.time()
#        print ('%s function took %0.3f ms' % (f.__name__ , (time2-time1)*1000.0))
#        return ret
#    return wrap

import copy
class Node_BTree(object):
    def __init__(self, data = None, left_node = None, right_node = None):
        self.data = data
        self.left = left_node
        self.right = right_node
        self.dict = {data:self}
        self.depth = {1:[1]}
        self.inorder_dict = {}
    
#    @timing    
    def get_node_index(self, index):
        return self.dict[index]

    def Insert(self, index, data, key):
        '''
        Insert a newNode with data at Index with Key = left or right
        Input 
        Index = 1 is root, Data(if -1 then put None), key = left or right

        output
        does not return anything
        '''
        new_node = Node_BTree(data)
        node = self.get_node_index(index)
        if key == 'left':
            node.left = new_node
            if index in self.inorder_dict.keys():
                self.inorder_dict[index]['left'] = data
            else:
                self.inorder_dict[index] = {}
                self.inorder_dict[index]['left'] = data                
        elif key == 'right':
            node.right = new_node
            if index in self.inorder_dict.keys():
                self.inorder_dict[index]['right'] = data
            else:
                self.inorder_dict[index] = {}
                self.inorder_dict[index]['right'] = data                
        self.dict[data] = new_node
        for key in self.depth.keys():
            if index in self.depth[key]:
                node_depth = key
        new_node_depth = node_depth + 1
        if new_node_depth in self.depth.keys():
            self.depth[new_node_depth].append(data)
        else:
            self.depth[new_node_depth] = []
            self.depth[new_node_depth].append(data)


    def getMaxDepth(self):
        return len(self.depth)

    def inorder_print(self):
        depth = self.getMaxDepth()
        inorder_string = copy.deepcopy(self.inorder_dict)
        while depth > 1:
            indexes_atDless1 = self.depth[depth-1]
            for index in indexes_atDless1:
                if index in inorder_string.keys():                
                    index_item = inorder_string[index]
                    if 'left' in index_item.keys() and 'right' in index_item.keys():
                        if index_item['left'] in inorder_string.keys():
                            inorder_string[index]['left'] = inorder_string[index_item['left']]
                        if index_item['right'] in inorder_string.keys():
                            inorder_string[index]['right'] = inorder_string[index_item['right']]
                        inorder_string[index] = str(index_item['left']) + ' ' +\
                    str(index) + ' ' + str(index_item['right'])
                    elif 'left' in index_item.keys() and 'right' not in index_item.keys():
                        if index_item['left'] in inorder_string.keys():
                            inorder_string[index]['left'] = inorder_string[index_item['left']]
                        inorder_string[index] = str(index_item['left']) + ' ' +\
                    str(index)
                    elif 'right' in index_item.keys():
                        if index_item['right'] in inorder_string.keys():
                            inorder_string[index]['right'] = inorder_string[index_item['right']]
                        inorder_string[index] = str(index) + ' ' + str(index_item['right'])
            depth -= 1
        print(inorder_string[1])
                    
        
        
    def swap_node(self, index):
        '''
        swap a particular node at given index
        Input 
        self, index at which to perform swap
        
        Output 
        does not return anything
        '''
        node = self.get_node_index(index)
        temp = node.left
        node.left = node.right
        node.right = temp

    
    def get_nodes_list_atDepth(self, depth):
        index_list = self.depth[depth]
        nodes_list = []        
        for index in index_list:
            if self.get_node_index(index):
                nodes_list.append(self.get_node_index(index))
        return nodes_list
                    
    def swap_depth(self, depth):
        '''
        swap all nodes at a particular depth
        Input 
        Self, Depth
        
        Output 
        does not return anything
        '''
        node_list_depth = self.get_nodes_list_atDepth(depth)
        for node in node_list_depth:
            if node is not None:
                temp = node.left
                node.left = node.right
                node.right = temp
        index_list = self.depth[depth]
        for index in index_list:
            if index in self.inorder_dict.keys():
                index_dict = self.inorder_dict[index]
                if 'right' in index_dict.keys() and 'left' in index_dict.keys():
                    index_dict['left'], index_dict['right'] = index_dict['right'], index_dict['left']
                elif 'right' in index_dict.keys() and 'left' not in index_dict.keys():
                    index_dict['left'] = index_dict['right']
                    del(index_dict['right'])
                elif 'left' in index_dict.keys() and 'right' not in index_dict.keys():
                    index_dict['right'] = index_dict['left']
                    del(index_dict['left'])

if __name__ == '__main__':
    N = int(input())
    new_tree = Node_BTree(1)
    for node_index in range(1, N+1):
        a, b = map(int, input().split())
        if b != -1:
            new_tree.Insert(node_index, b, 'right')
        if a != -1:
            new_tree.Insert(node_index, a, 'left')
    T = int(input())
    for _ in range(T):
        K = int(input())
        n = 1
        depth = new_tree.getMaxDepth()
        while n*K < depth:
            new_tree.swap_depth(n*K)
            n += 1
        new_tree.inorder_print()
        
        
'''
another implementation by https://www.hackerrank.com/hsiung 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class Node:
    nodes = []

    def __init__(self,i,a,b):
        self.val = i
        self.l = a
        self.r = b
        self.depth = None
        Node.nodes.append(self)
        
    def left(self):
        if self.l == -1:
            return None
        return Node.nodes[self.l-1]

    def right(self):
        if self.r == -1:
            return None
        return Node.nodes[self.r-1]

    @classmethod
    def inorder(cls):    
        stack = []
        node = cls.head()
        while 1:            
            while node is not None:
                stack.append(node)
                node = node.left()
            if len(stack) == 0:
                return
            node = stack.pop()
            sys.stdout.write("%d " % node.val)
            node = node.right()               

    @classmethod
    def head(cls):
        return cls.nodes[0]
    
    def swap(self):
        tmp = self.l
        self.l = self.r
        self.r = tmp
        
    @classmethod
    def BFS(cls, k):
        depth_nodes = []
        depth = 1
        n = Node.head()
        n.depth = depth
        depth_nodes.insert(0,n)
        while len(depth_nodes) > 0:
            n = depth_nodes.pop()
            if n.depth % k == 0:
                n.swap()
                
            l = n.left()
            if l:
                l.depth = n.depth+1
                depth_nodes.append(l)
            r = n.right()
            if r:
                r.depth = n.depth+1
                depth_nodes.append(r)
                
N = int(raw_input())
for i in xrange(1,N+1):
    a,b = map(int, raw_input().split(" "))
    Node(i,a,b)
    
T = int(raw_input())
for i in xrange(T):
    k = int(raw_input())
    Node.BFS(k)
    Node.inorder()
    sys.stdout.write("\n")
'''

'''

awesome implementation by https://www.hackerrank.com/spedl 

from collections import deque

class Node:
    def __init__(self, index):
        self.left = None
        self.right = None
        self.index = index
        
    
def in_order_traverse(root):
    """Don't use recursion b/c of recursion limit."""
    stack = deque([root])
    visited = set()
    while stack:
        node = stack.pop()
        if node is None:
            continue
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
        if node is None:
            continue
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
    n.left_index, n.right_index = [v if v > 0 else 0 for v in map(int, input().split())]
    nodes[i] = n

# fill out node objects
for n in nodes[1:]:
    left = nodes[n.left_index]
    right = nodes[n.right_index]
    n.left = left
    n.right = right

T = int(input())
root = nodes[1]
# do the swapping
for _ in range(T):
    k = int(input())
    swap(root, k)
    in_order_traverse(root)
    print('')
    
        
        
'''

'''
another one by https://www.hackerrank.com/LittleFox 
def inorder(T) :
    stack = [1]
    result = []
    while stack :
        i = stack.pop()
        if i > 0 :
            if T[i][1] > 0 : 
                stack.append(T[i][1])
            stack.append(-i)
            if T[i][0] > 0 : 
                stack.append(T[i][0])
        else :
            result.append(-i)
    return result

def swap(T, K) :
    toVisit, depth = [1], 1
    while toVisit :
        if depth % K == 0 :
            for i in toVisit :
                T[i] = (T[i][1], T[i][0])
        toVisit_ = []
        for i in toVisit :
            if T[i][0] > 0 :
                toVisit_.append(T[i][0])
            if T[i][1] > 0 :
                toVisit_.append(T[i][1])
        toVisit = toVisit_
        depth += 1

N = int(input())
T = [None] + [tuple(int(_) for _ in input().split()) for _ in range(N)]

N = int(input())
for _ in range(N) :
    swap(T,int(input()))
    print(" ".join(str(_) for _ in inorder(T)))
    
'''