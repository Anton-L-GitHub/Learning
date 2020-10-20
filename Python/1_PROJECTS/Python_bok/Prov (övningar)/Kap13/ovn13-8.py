import math
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def avstånd(self):
        return math.sqrt(self.x **2 + self.y ** 2)
    
    def flytta_horisontellt(self, d):
        self.x += d

    def flytta_vertikalt(self, d):
        self.y += d

class Figur:
    def __init__(self, x, y):
        self.startpunkt = Punkt(x, y)

class Cirkel(Figur):
    def __init__(self, r, x = 0, y = 0): 
        super().__init__(x, y)
        self.radie = r

    def area(self):
        return math.pi * self.radie ** 2

class Triangel(Figur):
    def __init__(self, b, h, x = 0, y = 0): 
        super().__init__(x, y)
        self.bas = b
        self.höjd = h

    def area(self):
        return self.bas * self.höjd / 2

class Rektangel(Figur):
    def __init__(self, b, h, x = 0, y = 0): 
        super().__init__(x, y)
        self.bredd = b
        self.höjd = h

    def area(self):
        return self.bredd * self.höjd 

# Test
figurer = [Cirkel(2), Triangel(3, 5, 1, 1), Rektangel(10, 20)]
for f in figurer:
    print(f.area())
