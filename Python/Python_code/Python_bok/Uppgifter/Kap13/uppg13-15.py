class Hus:
    def __init__(self, l, b):
        self.längd = l
        self.bredd = b

    def kvadratiskt(self):
        return self.längd == self.bredd

    def yta(self):
        return self.längd * self.bredd

    __yta = yta      # privat klassvariabel

    def __str__(self):
        y = self.__yta()
        return f'Hus med basytan {y:.1f}'

class Flervåningshus(Hus):
    def __init__(self, l, b, v):
        super().__init__(l, b)
        self.__antal = v             # antalet våningar

    def höghus(self):
        return self.__antal >= 10

    def yta(self):
        return self.längd * self.bredd * self.__antal

    __yta = yta

    def __str__(self):
        y = self.__yta()
        return super().__str__() + \
               f' och Flervåningshus med golvytan {y:.1f}'


class Hyreshus(Flervåningshus):
    def __init__(self, l, b, v, n):
        super().__init__(l, b, v)
        self.antal = n       # antalet lägenheter

    def yta(self):
        return super().yta() * 0.95

    def __str__(self):
        y = self.yta()
        return super().__str__() + \
                   f' och Hyreshus med lägenhetsytan {y:.1f}'

h = Hus(25, 10)
f = Flervåningshus(25, 10, 3)
hy = Hyreshus(25, 10, 3, 15)
print(h)
print(f)
print(hy)