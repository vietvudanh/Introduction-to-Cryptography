# coding=utf-8
"""Finding big prime number
"""

__author__ = 'Viet Vu Danh'
__email__ = 'vietvudanh@gmail.com'

# Fermat test
def is_prime(num):
    if num == 2:
        return True
    if not num & 1:         # divided by 2
        return False
    return pow(2, num-1, num) == 1

# Find next prime
def find_prime(n):
    if is_prime(n):
        n += 2
    while( not is_prime(n)):
        n += 2
    return n
    
a = 10**30 - 1    
        
for i in range(5):
    a = find_prime(a)
    print a
    
# Result
# 1000000000000000000000000000057
# 1000000000000000000000000000099
# 1000000000000000000000000000211
# 1000000000000000000000000000231
# 1000000000000000000000000000271