# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 22:13:46 2016

@author: bhupeshgupta
"""

import re 

def validate_roman(S):
    is_roman = True 
    is_roman =  False if (re.match(r'(?![MDCLXVI])', S) or re.search(r'M{4}|I{4}|C{4}|X{4}|L{2}|V{2}|D{2}', S)) else True    
    if is_roman:
        is_roman = False if ((re.search(r'((?<=[LDXVI])(M))', S)) or \
        (re.search(r'((?<=[LVI])(C))', S)) or (re.search(r'((?<=[LXVI])(D))', S)) or \
        (re.search(r'((?<=[V])(X))', S)) or re.search(r'((?<=[VI])(L))', S)) else True  
    return is_roman

S = input()
print(validate_roman(S))


'''
final answer by editor 

import re
print bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",raw_input()))

very elegant. But i am happy i tried and came this far. learnt alot. 
Regex still a mystery but i think we need to make the rules and then see how a pattern can represent it. 
'''