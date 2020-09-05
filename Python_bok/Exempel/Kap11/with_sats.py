# Demo av with-sats
n1 = input('Infilens namn? ' )
n2 = input('Utfilens namn? ')
with open(n1, 'r') as f1, open(n2, 'w') as f2:
    r, t = 0, 0       # antal rader och tecken
    for rad in f1:
        t += f2.write(rad)
        r += 1
    print(f'{r} rader och {t} tecken kopierade') 