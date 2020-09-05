n = input('Filens namn? ' )
with open(n, 'r') as f:
    ut = []
    for rad in f:
        s = rad.replace('\t', '   ')
        ut += [s]
with open(n, 'w') as f:
    for rad in ut:
        f.write(rad)