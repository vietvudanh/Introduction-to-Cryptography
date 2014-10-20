"""Module to find primitive roots of a prime number
Method: Find prime factors, test with each to decide

Usage: python primitive_root.py <number>

Drawbacks: Cannot deal with prime greater than 32-bit length. Is there any suggestion?
"""
import sys

__author__ = 'Viet Vu Danh'
__email__ = 'vietvudanh@gmail.com'

n = int(sys.argv[1])	# n is prime
_n = n-1				# so phi(n) is n-1

def primeFactors(n):
	"""Find prime factors of n
	Params: prime n

	Return: list of factors

	"""
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    return list(set(factors))

if __name__ == '__main__':

	print range(n)
	# find prime factors
	factors = primeFactors(_n)
	for i in range(len(factors)):
		factors[i] = n / factors[i]

	# perform test on prime number
	root = [2,3,5,6,7,11,13,17]

	for r in root:
		count = 0
		for f in factors:
			l = pow(r, f,n)
			if( l != 1):
				# print '%s^%s == %s mod %s' %(r, f, l, n)
				count += 1
		if(count == len(factors)):
			print r, 'is OK'
			break