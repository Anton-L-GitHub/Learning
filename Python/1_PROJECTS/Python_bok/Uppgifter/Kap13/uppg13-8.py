class Rektangel:
    def __init__(self, x=0, y=0, h=0, b=0):
        self.x = x
        self.y = y
        self.set_h(h)
        self.set_b(b)

    def set_h(self, h):
        assert(h >= 0)
        self._h = h

    def set_b(self, b):
        assert(b >= 0)
        self._b = b

    def get_h(self):
        return self._h
    
    def get_b(self):
        return self._b   

    def area(self):
        return self._h * self._b

    def omkr(self):
        return 2*self._h + 2*self._b
