# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:07:39 2016

@author: bhupeshgupta
"""

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth        
    if len(elem) > 0: # if element has children the level increased by 1
        level += 1
    for child in elem: 
        if len(child) > 0: # if child has further children: 
            depth(child, level)  
    if level + 1  > maxdepth:
        maxdepth = level + 1
    return maxdepth

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

'''
We need to find maximum depth. i.e. depth of most nested element 
given an element and its level 
if that element has children then all its children are at level + 1 else level is same
'''