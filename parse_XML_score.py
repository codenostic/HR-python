# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:00:40 2016

@author: bhupeshgupta
"""

'''
learn how to parse XML and get its attributes
'''

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    total_attr = 0    
    for child in node:
        if len(child) > 1:
            total_attr += get_attr_number(child)
        else:
            total_attr += len(child.attrib)
    
    return total_attr + len(node.attrib)





if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    print(tree)
    root = tree.getroot()
    print(root)
    print(get_attr_number(root))
    
'''
another solution - plain and simple 
def count_of_attr(root):
    count = len(root.attrib)
    for child in root:
        count += count_of_attr(child)
    return count

then there are other iteraive solutins using .iter etc
'''