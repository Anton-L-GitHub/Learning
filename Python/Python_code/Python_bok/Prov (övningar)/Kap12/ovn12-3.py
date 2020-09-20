import json

tab = dict()
print('Skriv artikelbeteckning, antal och pris')
print("Avsluta med ''")
while True:
    s = input('>')
    if s == '':
        break
    r = s.split()
    k = r[0]
    v = [int(r[1]), float(r[2])]
    tab[k] = v

namn = input('Filnamn? ')
with open(namn, 'w') as f:
    json.dump(tab, f)