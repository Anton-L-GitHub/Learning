# Kopiera en fil till en annan
from sys import argv
if len(argv) != 3:
    print('Fel antal argument')
    exit()
with open(argv[1], 'r') as f1, open(argv[2], 'w') as f2:
    r, t = 0, 0       # antal rader och tecken
    for rad in f1:
        t += f2.write(rad)
        r += 1
    print(f'{r} rader och {t} tecken kopierade') 