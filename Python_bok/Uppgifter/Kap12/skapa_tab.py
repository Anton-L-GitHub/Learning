import json
# Steg 1, läs in tabellen eller skapa en ny
f_namn = input('Filen med resultat? ')
try:
    with open(f_namn, 'r') as f:  
        tab = json.load(f)         # läs in tabellen 
except FileNotFoundError:
    tab = dict()                   # skapa en tom tabell
# Steg 2, ändra i tabellen
print('Avsluta med tom rad')
while True:
    namn = input('Namn? ').lower()
    if namn == '':                
        break
    rad = input('Poäng? ')
    poängen = [int(p) for p in rad.split()] 
    tab[namn] = poängen
# Steg 3, lagra tabellen i filen
with open(f_namn, 'w') as f:
    json.dump(tab, f)