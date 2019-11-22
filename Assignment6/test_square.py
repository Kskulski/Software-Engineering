import unittest
from square import Square


class SquareTest(unittest.TestCase):
	def test_area(self):
		self.sq = Square(3)
		self.assertEqual(self.sq.area(), 9, "positive side length")
		self.sq = Square(-5)
		self.assertEqual(self.sq.area(), 25, "negative side length")
		self.sq = Square(0)
		self.assertEqual(self.sq.area(), 0, "zero side length")
		self.sq = Square(5.5)
		self.assertEqual(self.sq.area(), 30.25, "decimal side length")


if __name__ == '__main__':
	unittest.run()