# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:39:22 2016

@author: bhupeshgupta
"""

'''
group, groups, groupdict
Task
print first occurence of repeating AlphaNumeric character else print -1

alphanumeric means [a-zA_Z0-9]
'''
import re
strToSearch = input()
searchObj = re.search(r'([a-zA-Z0-9])\1', strToSearch)
print(searchObj.group(1) if searchObj else -1)
