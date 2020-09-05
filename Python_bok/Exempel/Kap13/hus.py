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

class Hyreshus(Flervåningshus):
    def __init__(self, l, b, v, n):
        super().__init__(l, b, v)
        self.lägenheter = n       # antalet lägenheter
        
    def yta(self):
       return super().yta() * 0.95