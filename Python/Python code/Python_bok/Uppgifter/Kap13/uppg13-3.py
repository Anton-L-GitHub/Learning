class Bil:
    def __init__(self):
        self.reg_nr = ''
        self.fabrikat = ''
        self.årsmodell = 0
        self.tjänstevikt = 0.0
        self.effekt = 0.0

b1 = Bil()
b2 = Bil()
b1.reg_nr = 'ABC123'
b1.fabrikat = 'Renault Megane'
b1.årsmodell = 2013
b1.tjänstevikt = 1460
b1.effekt = 81.0
b2.reg_nr = 'LYX999'
b2.fabrikat = 'Tesla Model S'
b2.årsmodell = 2019
b2.tjänstevikt = 2215
b2.effekt = 285.0
print(b1.reg_nr, b1.fabrikat, b1.årsmodell, b1.tjänstevikt, b1.effekt)
print(b2.reg_nr, b2.fabrikat, b2.årsmodell, b2.tjänstevikt, b2.effekt)
