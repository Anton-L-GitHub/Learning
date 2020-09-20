class Bil:
    def __init__(self, reg_nr, fabrikat, årsmodell, tjänstevikt, effekt):
        self.reg_nr = reg_nr
        self.fabrikat = fabrikat
        self.årsmodell = årsmodell
        self.tjänstevikt = tjänstevikt
        self.effekt = effekt

b1 = Bil('ABC123', 'Renault Megane', 2013, 1460, 81.0)
b2 = Bil('LYX999', 'Tesla Model S', 2019, 2215, 285.0)
print(b1.reg_nr, b1.fabrikat, b1.årsmodell, b1.tjänstevikt, b1.effekt)
print(b2.reg_nr, b2.fabrikat, b2.årsmodell, b2.tjänstevikt, b2.effekt)