# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 17:02:45 2017

@author: bhupeshgupta
"""

def inorder(T) :
    stack = [1]
    result = []
    # interesting, using -, + to segregate left right and arranging tree inorder    
    '''
    This is similar to recurrion step i.e. left then node then right 
    Only difference being
    1) we are maintaining the stack ourself so no overflow 
    2) maintaiing it in reverse with - = index unpacked and + = index tounpack 
    '''
    while stack :
        i = stack.pop() 
        if i > 0 : # if + then unpack (right and left) if -ve (means unpacked)store in result 
            if T[i][1] > 0 : # this is right index to be stored in stack
                stack.append(T[i][1])
            stack.append(-i) # this is the node in - as we have unpacked it
            if T[i][0] > 0 : # store left index at last because we need to unpack left most further
                stack.append(T[i][0])
        else :
            result.append(-i)
    return result

def swap(T, K) :
    toVisit, depth = [1], 1
    while toVisit :
        if depth % K == 0 : # when depth is multiple of k 
            for i in toVisit : # i = index in toVisit, and T[i]'s elements swapped
                T[i] = (T[i][1], T[i][0]) # this just swaps the tuple at Index i
        # till depth multiple of K, we fill toVisit with indexes at next depth
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
