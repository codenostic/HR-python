# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:25:17 2016

@author: bhupeshgupta
"""

'''
HEX color code  in CSS 
'''
import re 

#main function 

lines = int(input())
for _ in range(lines):
    line = input()
    if re.search(r'(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})', line):
        searchObj = re.findall(r'(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})', line)
        for color in searchObj :
            print(color)

'''
editors solution is similar to mine but he has mande the CSS in a long string an then RE on that

from __future__ import print_function
import re

css = ""
for i in range(int(raw_input())):
    css+=raw_input()
    css+='\n'

inside_brackets = re.findall(r'\{.*?\}', css, flags=re.DOTALL)
for property in inside_brackets:
    map(lambda i: print(i,sep='\n',end='\n'),(re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', property)))
'''