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

'''
my solution is pretty much best just see aother way to add decimal
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __div__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * Complex(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


C = map(float, raw_input().split())
D = map(float, raw_input().split())
x = Complex(*C)
y = Complex(*D)
print '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))
'''