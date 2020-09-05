class Bok:
    def __init__(self):
        self.titel = ''
        self.författare = ''
        self.antal_sidor = 0
        self.pris = 0.0

b1 = Bok()
b1.titel = 'Python från början'
b1.författare = 'Jan Skansholm'
b1.antal_sidor = 295
b1.pris = 275

b2 = Bok()
b2.titel = 'Mio, min Mio'
b2.författare = 'Astrid Lindgren'
b2.antal_sidor = 184
b2.pris = 159

print(f'{b1.titel} av {b1.författare}, '
      f'{b1.antal_sidor} sidor, {b1.pris} kr')

print(f'{b2.titel} av {b2.författare}, '
      f'{b2.antal_sidor} sidor, {b2.pris} kr')
