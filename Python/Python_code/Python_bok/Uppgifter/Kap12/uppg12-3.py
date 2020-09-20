import json
# Läs in tabellen eller skapa en ny
f_namn = input('Filen med resultat? ')
with open(f_namn, 'r') as f:  
    tab = json.load(f)         # läs in tabellen 
# Visa resultat
print('Avsluta med tom rad')
while True:
    namn = input('Namn? ').lower()
    if namn == '':                
        break
    print('Resultat:', tab[namn])