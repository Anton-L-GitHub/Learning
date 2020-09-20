n = input('Filens namn? ' )
with open(n, 'r') as f:
    for rad in f:
        s = rad.replace('\t', '   ')
        print(s, end='')