# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:58:10 2016

@author: bhupeshgupta
"""

'''
substitute i.e find and replace 
'''
import re 

def replace(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'

N = int(input()) 
contents = []
for _ in range(N):
    line = input()
    contents.append(line)
strToModify = '\n'.join(contents)


print(re.sub(r'(?<=\s)(&&)(?=\s)|(?<=\s)(\|\|)(?=\s)', replace, strToModify))


'''
editors solutions looks pretty neat and simple

import re

for line in range(int(raw_input())):
    string = ''
    string = re.sub(r'(?<= )&&(?= )','and',raw_input())
    string = re.sub(r'(?<= )\|\|(?= )','or',string)
    print string
'''