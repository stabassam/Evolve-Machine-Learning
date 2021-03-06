#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:08:38 2018

@author: stabassam
"""
from math import sqrt


class Vector(object):
    
    # Constructor
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates myst be non-empty')

    # Addition
    def plus(self,v):
        new_coordinates = [ x + y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    # Subtraction
    def minus(self,v):
        new_coordinates = [ x - y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    # Scalar Multiplication
    def times_scalar(self,c):
        new_coordinates = [ c * x for x in self.coordinates]
        return Vector(new_coordinates)
    
    # Magnitude
    def magnitude(self):
        coordinates_square = [x ** 2 for x in self.coordinates]
        return sqrt(sum(coordinates_square))

    # Find normalized direction
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    # Find dot product
    def dot_product(self,b):
        return sum([ x * y for x,y in zip(self.coordinates, b.coordinates)])

    # String Representation Format
    def __str__(self):
        return 'Vector : {0}' . format(self.coordinates)
    
    # Comparator
    def __eq__(self, v):
        return self.coordinates == v.coordinates


my_vector = Vector([1, 2, 3, 4])
print(my_vector)

my_vector2 = Vector([1, 2, 3, 4])
print(my_vector == my_vector2)

v = Vector([8.218, 4.138])
w = Vector([-8.802, 6.776])

print(v.plus(w))            
print(v.magnitude())


print("\n\nDot product:")
a = Vector([7.887, 4.138])
b = Vector([-8.802, 6.776])

print(a.dot_product(b))
