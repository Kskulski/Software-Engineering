import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return math.pow(self.side, 2)

    def circumference(self):
        return self.math_util.add(2 * self.side, 2 * self.side)
