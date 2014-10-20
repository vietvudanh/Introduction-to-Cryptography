"""
RSA Encryption and Decryption scheme
"""
import string

__author__ = 'Viet Vu Danh'
__email__ = 'vietvudanh@gmail.com'

x = int(sys.argv[0])

p = 1001246549
q = 104393329

n = p * q
_n = (p-1)*(q-1)				# phi(n)

e = 101 						# random
d = 46569858101390380			# calculated by Euclid Extend Algorithm

_a = 2							# alpha primitive root of p
a = 1002 						# a

def string_to_number(msg):
	"""convert string to number"""
	_lower = string.ascii_lowercase
	_number = 0
	for i in msg:
		_number += _lower.index(i) * ( 10** (len(msg) - msg.index(i) ) )
	return _number

def encrypt(msg):
	global n, e 				# public (n, e)
	print 'encrypt: %s with n = %s, e = %s. c = m^e mod n' % (msg, n, e)
	c = pow(msg ,e, n)
	print 'c = %s' % c
	return c

def decrypt(c):
	global n, d 				# decrypt using secret d
	print 'decrypt c = %s, with n = %s, d= %s. m = c^e mod n'
	m = pow(c, d, n)
	print 'm = %s' % m
	return m

if __name__ == '__main__':
	message = 'vudanhviet'
	_message = string_to_number(message)
	c = encrypt(_message)
	m = decrypt(c)