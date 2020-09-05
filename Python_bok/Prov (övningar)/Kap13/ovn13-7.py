class Djur:
    def __init__(self, längd, vikt):
        self.längd = längd
        self.vikt = vikt

class Däggdjur(Djur):
    def __init__(self, längd, vikt):
        super().__init__(längd, vikt)   

class Kräldjur(Djur):
    def __init__(self, längd, vikt):
        super().__init__(längd, vikt) 

class Fågel(Djur):
    def __init__(self, längd, vikt):
        super().__init__(längd, vikt) 

class Hund(Däggdjur):
    def __init__(self, längd, vikt, ras):
        super().__init__(längd, vikt)
        self.ras = ras

    def läte(self):
        if self.vikt < 3:
            return 'Viff'
        elif self.vikt < 10:
            return 'Vov'
        else:
            return 'VOFF'

class Orm(Kräldjur):
    def __init__(self, längd, vikt, giftig):
        super().__init__(längd, vikt)
        self.giftig = giftig

    def läte(self):
        if self.giftig:
            return 'SSSSSSS...'
        else:
            return 'sssssss...'      

class Kråka(Fågel):
    def __init__(self, längd, vikt):
        super().__init__(längd, vikt)

    def läte(self):
        return 'Krax, Krax'

# Test
l = [Hund(0.50, 8, 'Tax'), Kråka(0.50, 0.5), 
     Orm(2, 1.5, True), Hund(0.95, 45, 'Rottweiler')]
for d in l:
    print(d.läte())
