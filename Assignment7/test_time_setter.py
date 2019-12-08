import unittest
from time_setter import TimeSetter

class TimeSetterTest(unittest.TestCase):
    def setUp(self):
        self.time_setter = TimeSetter()


    def test_add_366(self):
        result = self.time_setter.convert(366)
        self.assertEqual(result, 1981)

    def test_add_365(self):
        result = self.time_setter.convert(365)
        self.assertEqual(result, 1980)

    def test_add_less_than_year(self):
        result = self.time_setter.convert(10)
        self.assertEqual(result, 1980)

    def test_zero_days(self):
        result = self.time_setter.convert(0)
        self.assertEqual(result, 1980)

    def test_add_negative_days(self):
        result = self.time_setter.convert(-1)
        self.assertEqual(result, 1980)

    def test_add_two_years_non_leap(self):
        result = self.time_setter.convert(731)
        self.assertEqual(result, 1981)


    def test_add_two_years_leap(self):
        result = self.time_setter.convert(732)
        self.assertEqual(result, 1982)


    def test_add_four_years(self):
        result = self.time_setter.convert(1825)
        self.assertEqual(result, 1984)



