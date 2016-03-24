import unittest
from utils import string_to_number


class TestStringToNumber(unittest.TestCase):

    test_cases_true = [
        ('abc', 28),
        ('efg', 2840),
        ('xyzwf', 10949749)
    ]

    def test_true(self):
        for char, num in TestStringToNumber.test_cases_true:
            self.assertEqual(string_to_number.string_to_number(char), num)
