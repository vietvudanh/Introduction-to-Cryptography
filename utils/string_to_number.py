"""Module to convert string to number.
Method: mapping character in ASCII, lowercase: [a-z] in to 26-based

Usage: python string_to_number.py <string>
"""
import string
import sys


def string_to_number(msg):
    """convert string to number"""
    _lower = string.ascii_lowercase
    _number = 0
    for i in msg:
        _number += _lower.index(i) * (26 ** (len(msg) - msg.index(i) - 1))
    return _number


if __name__ == '__main__':
    msg = sys.argv[1]
    print string_to_number(msg)
