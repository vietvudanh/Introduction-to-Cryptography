"""Vigenere encoding
"""

# coding=utf-8
import string

__author__ = 'Viet Vu Danh'
__email__ = 'vietvudanh@gmail.com'

_source = "this is just a random text"
source = list(_source)
_keyword = "vietvudanh"
keyword = list(_keyword)

lower = string.ascii_lowercase

number_source = []
char_source = []

for i in range(len(source)):
	if(source[i] == ' '):
		number_source.append(-1)
		continue
	number_source.append(lower.index(source[i]))

i = 0

while( i < len(number_source)):
	for j in range(len(keyword)):
		if( i == len(number_source)):
			break
		if(number_source[i] == -1):
			char_source.append(" ")
			i += 1
			continue
		number_source[i] = (number_source[i] + lower.index(keyword[j]) ) % len(lower)
		char_source.append( lower[number_source[i]] )
		i += 1

print 'Source:', _source
print 'keyword', _keyword
print 'After::',''.join(char_source)