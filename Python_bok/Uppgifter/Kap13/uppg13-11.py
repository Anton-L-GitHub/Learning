from math import pi
class Cirkel:
    def __init__(self, x=0, y=0, radie=0):
        self.x = x
        self.y = y
        self.set_r(radie)
    def get_r(self):
        return self._r          
    def set_r(self, r):
        assert r >= 0, ('Negativ radie', r)
        self._r = r 
    def area(self):
        return pi * self._r ** 2
    def omkr(self):
        return 2 * pi * self._r
    def __eq__(self, other):
        return self._r == other._r
    def __lt__(self, other):
        return self._r < other._r
# Nya metoder:
    def __ge__(self, other):
        return not self < other
    def __le__(self, other):
        return self < other or self == other
    def __gt__(self, other):
        return not self <= other
  