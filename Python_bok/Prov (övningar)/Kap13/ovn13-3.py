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
    
# Test
p = Punkt(1, 1)
print(p.avstånd())
p.flytta_horisontellt(3)
p.flytta_vertikalt(-2)
print(p.x, p.y)