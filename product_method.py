# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 18:13:23 2016

@author: bhupeshgupta
"""
# original implementation
#def product(*args, repeat=1):
#    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
#    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
#    pools = [tuple(pool) for pool in args] * repeat
#    result = [[]]
#    for pool in pools:
#        result = [x+[y] for x in result for y in pool]
#    print(result)

def product_iter(*args, repeat=1):
    '''
    objective - catersian product of arguments 
    inputs - iterable arguments such as string, list, tuple, dict etc 
    output - cartesian product of arguments
    
    solution
    1) we make a list of tuples, converting each argument to tuple to separate out the elements
    2) Make a list of list, where each element of a new tuple added to every element present in list
    This looks like recurssion 
    
    '''
    
    pools = [tuple(pool) for pool in args]*repeat

    result = [[]]
    for pool in pools:
        for x in result:
            for y in pool:
                result = result + [x + [y]]
            result.remove(x)
    print(result)


product_iter('ABCD','xy')


'''
comments 
finally got this bitch. Nice one. This is fucking gonna help me in learning 
builtins and python. Yo ho. I find groupby and product pretty useful like all itertools.
'''