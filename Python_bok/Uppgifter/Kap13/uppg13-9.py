class Rektangel:
    def __init__(self, x=0, y=0, h=0, b=0):
        self.x = x
        self.y = y
        self.h = h
        self.b = b

    @property
    def h(self):
        return self._h

    @property
    def b(self):
        return self._b

    @h.setter
    def h(self, h):
        assert(h >= 0)
        self._h = h

    @b.setter
    def b(self, b):
        assert(b >= 0)
        self._b = b

    def area(self):
        return self.h * self.b

    def omkr(self):
        return 2*self.h + 2*self.b
    
