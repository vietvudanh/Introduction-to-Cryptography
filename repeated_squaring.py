# coding=utf-8
"""Repeated squaring method
Usage: repeated_squaring x d n 
for finding x^d (mod n)
"""

__author__ = 'Viet Vu Danh'
__email__ = 'vietvudanh@gmail.com'

import sys

# input
x = int(sys.argv[1])
d = int(sys.argv[2])
n = int(sys.argv[3])

_digits = bin(d)[2:]
digits = []

# convert to int
for i in range(len(_digits)):
    digits.append( int(_digits[i]) )

digits = [i for i in reversed(digits)]    

k = len(digits)
_x = list()
_c = list()

_c.append(1 * x**digits[0])

_x.append(x)

print(0, digits[0], _c[0], _x[0],)
for j in range(1, k):
    _x.append( (_x[j-1]**2) % n )
    _c.append( (_x[j]**digits[j]  * _c[j-1]) % n )
    print(j, digits[j], _c[j], _x[j],)

print("method:" ,_c[k-1])        # result of method
print("built-in:", pow(x, d, n))    # python built-in function

# both return 345, which mean the implementation is right                    
