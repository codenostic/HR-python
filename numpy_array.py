# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:11:11 2017

@author: bhupeshgupta
"""

import numpy
list = [float(x) for x in input().split()]
list.reverse()
a = numpy.array(list)

'''
interesting solutions 
import numpy

print numpy.array(raw_input().split(),float)[::-1]

OR 

import numpy

print numpy.flipud(numpy.array(raw_input().split(),float))
'''