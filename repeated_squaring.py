# coding=utf-8
"""Repeated squaring method
Usage: repeated_squaring x d n 
for finding x^d (mod n)
"""

__author__ = 'Viet Vu Danh'
__email__ = 'vietvudanh@gmail.com'

import string
import sys

# input
x = int(sys.argv[1])
d = int(sys.argv[2])
n = int(sys.argv[3])

# constants
digs = string.digits + string.lowercase

# convert base
def int2base(x, base):
    if x < 0: sign = -1
    elif x==0: return '0'
    else: sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
        if sign < 0:
            digits.append('-')
            digits.reverse()
    return digits

digits = int2base(d, 2)

# convert to int
for i in range(len(digits)):
    digits[i] = int(digits[i])

k = len(digits)
_x = list()
_c = list()

if( digits[0] == 1):
    _c.append(x)
else:
    _c.append(1)

_x.append(x)

for j in range(1, k):
    _x.append( (_x[j-1]**2) % n )
    if(digits[j] == 1):
        _c.append( (_x[j] * _c[j-1]) % n )
    else:
        _c.append( _c[j-1] % n )

print _c[k-1]        # result of method
print pow(x, d, n)    # python built-in function

# both return 345, which mean the implementation is right                    