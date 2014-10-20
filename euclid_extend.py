#!/usr/bin/python
# coding=utf-8    

"""Euclid extend algorithms
Usage: euclid_extend a, b for calculating b^-z (mod a)
"""
import math
import sys

__author__ = 'Vu Danh Viet'
__email__ = 'vietvudanh@gmail.com'
__description__ = 'Euclid extend algorithms script'

# a, b, d, r, q
# x, y, x1, x2, y1, y2

_a = int(sys.argv[1])
_b = int(sys.argv[2])
a = _a
b = _b

# initialize
x2 = 1
x1 = 0
y2 = 0
y1 = 1

while( b > 0):
    q = math.floor( a / b)
    r = a % b
    x = x2 - q * x1
    y = y2 - q * y1
    a = b
    b = r
    x2 = x1
    x1 = x
    y2 = y1
    y1 = y

d = a
x = x2
y = y2

print a, x, y
print _b,'^-1', 'mod', _a, '=', _a + y if(y < 0) else y