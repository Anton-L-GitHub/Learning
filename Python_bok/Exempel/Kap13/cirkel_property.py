from math import pi
class Cirkel:
    def __init__(self, x=0, y=0, radie=0):
        self.x = x
        self.y = y
        self.r = radie

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        assert r >= 0, ('Negativ radie', r)
        self._r = r

    def area(self):
        return pi * self.r ** 2
        
    def omkr(self):
        return 2 * pi * self.r