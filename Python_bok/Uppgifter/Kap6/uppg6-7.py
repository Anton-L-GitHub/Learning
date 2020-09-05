# Inläsning till en matris
print('Skriv en matris rad för rad. ' 
      'Avsluta med en tom rad.')
m = []
while True:
    s = input('? ')
    if s == '':
        break
    s = s.replace(' ', '')
    ls = s.split(',')             # lista med texter
    rad = [float(e) for e in ls]  # lista med float
    m.append(rad)                 # ny rad i matrisen
print(m)