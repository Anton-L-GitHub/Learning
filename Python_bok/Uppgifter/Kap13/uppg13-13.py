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

sk = Skola(0, 0, 3, 10)
print(sk.klassrum_per_vån())
sk.bredd = 15
print(sk.antal_klassrum)
f = Flervåningshus(0, 0, 3)
f.bredd = 15
print(f.antal_klassrum)   # Denna rad ger en felutskrift

