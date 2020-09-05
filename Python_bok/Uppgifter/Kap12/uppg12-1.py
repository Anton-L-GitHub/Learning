print('Skriv in flaggornas färger. Avsluta med en tom rad')
flaggor = []
while True:
    s = input('> ')
    if s == '':
        break
    ordlist = s.split()         # en lista med orden
    färger = set(ordlist)       # en mängd med orden
    flaggor.append(färger)
alla = set()
gemensamma = flaggor[0]
for f in flaggor:
    alla = alla | f
    gemensamma = gemensamma & f
print('Alla färger:', alla)
print('Gemensam färg:', gemensamma)