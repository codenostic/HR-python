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
    pass # your code goes here



if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))