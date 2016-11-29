# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:47:59 2016

@author: bhupeshgupta
"""

'''
torsional Angle - 
Given point A,B,C,D find 
angle between plane ABC and BCD in degrees - Let it be PHI

the cos(PHI) = X.Y/|X|*|Y|
X = AB X BC and Y = BC X CD
AB = B - A 

cool so what we need is to 
1) make a data type Vector which takes x, y and z arguments 
2) Methods we need - Vector Sum, Vector substraction, crossproduct, dotproduct, vector magnitude
3) then we will need acos of cos_phi using above formula and get radians and then turn radian to degrees 
'''
import math 

class Vector:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
        
    def __sub__(self,other):
        return Vector(other.x-self.x, other.y-self.y, other.z-self.z)
    
    def cross_product(self, other):
        return Vector((self.y*other.z - self.z*other.y), (self.z*other.x - self.x*other.z), \
        (self.x*other.y-self.y*other.x))
    
    def dot_product(self, other):
        return (self.x*other.x + self.y*other.y + self.z*other.z)
    
    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

# main function starts here 
a1, a2, a3 = map(float, input().split())
b1, b2, b3 = map(float, input().split())
c1, c2, c3 = map(float, input().split())
d1, d2, d3 = map(float, input().split())

A = Vector (a1, a2, a3)
B = Vector (b1, b2, b3)
C = Vector (c1, c2, c3)
D = Vector (d1, d2, d3)

AB = B - A
BC = C - B
CD = D - C

X = AB.cross_product(BC)
Y = BC.cross_product(CD)

cos_phi = (X.dot_product(Y))/(X.length()*Y.length())

PHI = math.acos(cos_phi)  # angle in radians 

print(round(math.degrees(PHI), 2))  # angle in degrees