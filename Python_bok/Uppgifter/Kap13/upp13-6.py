class Rektangel:
    def __init__(self, x=0, y=0, h=0, b=0):
        self.x = x
        self.y = y
        self.h = h
        self.b = b

    def set_h(self, h):
        assert(h >= 0)
        self.h = h

    def set_b(self, b):
        assert(b >= 0)
        self.b = b

    def area(self):
        return self.h * self.b

    def omkr(self):
        return 2*self.h + 2*self.b
    