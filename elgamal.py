#!/usr/bin/python
"""
ElGamal Encryption and Signature scheme
"""
import string

__author__ = 'Viet Vu Danh'
__email__ = 'vietvudanh@gmail.com'

p = 2038072819					# prime number, has length > 10

_a = 5							# alpha primitive root of p
a = 1002 						# a
pub_key = []					# public
pub_key.append(p)
pub_key.append(_a)
pub_key.append(pow(_a, a, p))

def string_to_number(msg):
	"""convert string to number"""
	_lower = string.ascii_lowercase
	_number = 0
	for i in msg:
		_number += _lower.index(i) * ( 26** (len(msg) - msg.index(i) -1) )
	return _number

def encrypt(msg):
	"""ElGamal encryption"""
	global pub_key		# pub key is (p, alpha, alpha^a)
	print 'encrypt: %s p = %s, alpha = %s, alpha^a = %s, pubkey = %s' % (msg, pub_key[0], pub_key[1], pub_key[2], pub_key)
	b = 1115
	c = []
	c.append(pow(pub_key[1], b, pub_key[0]))
	c.append(msg * pow(pub_key[2], b, pub_key[0])%p)
	print 'c = ', c
	print ''
	return c

def decrypt(c):
	"""ElGamal decryption"""
	global p, _a, a			# secret key 
	print 'decrypt c = %s, with a = %s' %(c, a)
	_c = pow(c[0], p-1-a, p)
	print '(alpha^b)-a = ', _c
	m = (_c * c[1] ) % p
	print 'm = ', m
	print ''
	return m

def sign(msg):
	"""ElGamal Signature scheme"""
	global pub_key, a		# public key
	r = 101					# random
	_r = 1553778287			# r^-1 mod p
	_b = pow(pub_key[1], r, pub_key[0])
	_g = ((msg - a*_b) * _r)%(pub_key[0]-1)

	sign = [_b, _g]
	print 'sign = ', sign
	return sign

def check(sign, msg):
	"""ElGamal signature check scheme"""
	global pub_key			# pub key: (p, alpha, y)
	print 'check sign with sign = ', sign, ' msg = ', msg
	if( p % sign[0] == 0):
		print 'beta is divided by p'
		return
	_d = (pow(pub_key[2], sign[0], pub_key[0]) * pow( sign[0], sign[1],pub_key[0] ) ) % pub_key[0]
	_s = pow(pub_key[1], msg, pub_key[0])
	print 'delta = %s, sigma = %s' % ( _d, _s)
	if( _d == _s):
		print 'True'
		return True
	else:
		print False
		return False

if __name__ == '__main__':
	message = 'vdviet'
	_message = string_to_number(message)
	c = encrypt(_message)
	m = decrypt(c)

	sign = sign(_message)
	check(sign, _message)

# OUTPUT:
# encrypt: 500394251 p = 2038072819, alpha = 5, alpha^a = 1743460162, pubkey = [2038072819, 5, 1743460162L]
# c =  [715069332L, 559551216L]
# decrypt c = [715069332L, 559551216L], with a = 1002
# (alpha^b)-a =  1330611742
# m =  500394251
# sign =  [1453843825L, 1018560271L]
# check sign with sign =  [1453843825L, 1018560271L]  msg =  500394251
# delta = 346315180, sigma = 346315180
# True