import random
namn = input('Filens namn? ' )
with open(namn, 'r') as f:
    antal = 0
    for r in f:
        antal += 1
with open(namn, 'r') as f:
    k = random.randint(1, antal)
    print(antal, k)
    for i in range(1, k+1):
        r = f.readline()
    print(r)   