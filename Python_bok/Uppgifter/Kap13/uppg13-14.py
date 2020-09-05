class Hus:
    def __init__(self, l, b):
        self.längd = l
        self.bredd = b
    def kvadratiskt(self):
        return self.längd == self.bredd
    def yta(self):
        return self.längd * self.bredd

class Flervåningshus(Hus):
    def __init__(self, l, b, v):
        super().__init__(l, b)
        self.antal = v             # antalet våningar
    def höghus(self):
        return self.antal >= 10
    def yta(self):
        return self.längd * self.bredd * self.antal

class Skola(Flervåningshus):
    def __init__(self, l, b, v, n):
        super().__init__(l, b, v)
        self.antal_klassrum = n     
    def klassrum_per_vån(self):
        return self.antal_klassrum / self.antal
    def yta(self):
        return self.antal_klassrum * 50

l = [Hus(50, 30), Skola(50, 30, 3, 10)]
for e in l:
    print(e.yta())