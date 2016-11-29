# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 18:03:19 2016

@author: bhupeshgupta
"""

'''
implement complex numbers
'''

class ComplexNumber:
    def __init__(self, realpart, imgpart):
        self.r = realpart
        self.i = imgpart
    
    def __add__(self, other):
        return ComplexNumber(self.r + other.r, self.i+other.i)
    
    def __str__(self):
        if self.i >= 0:
            return (str(format(float(self.r),'.2f')) + '+' + str(format(float(self.i),'.2f'))+'i')
        else: 
            return (str(format(float(self.r),'.2f'))+str(format(float(self.i),'.2f'))+'i')
    
    def __sub__(self,other):
        return ComplexNumber(self.r - other.r, self.i - other.i)
    
    def __mul__(self, other):
        return ComplexNumber(self.r*other.r - self.i*other.i, self.r*other.i + self.i*other.r)
    
    def __truediv__(self, other):
        
        return ComplexNumber((self.r*other.r + self.i*other.i)/(other.r**2 + other.i**2), (-self.r*other.i + self.i*other.r)/(other.r**2 + other.i**2))
        
    def __abs__(self):
        return ComplexNumber((self.r**2+self.i**2)**0.5, 0.00)

#main functions starts here 
c1, c2 = map(float, input().split())
C = ComplexNumber(c1,c2)
d1,d2 = map(float, input().split())
D = ComplexNumber(d1,d2)

print(C + D)
print(C - D)
print(C*D)
print(C/D)
print(abs(C))
print(abs(D))