n = input('Filens namn: ')
with open(n, 'r') as f:
    r, k = 0, 0     # antal rader, rader med kommentarer
    for rad in f:
        r += 1
        if rad.find('#') >= 0:
            k += 1
    print(f'{k/r*100:.1f} % av raderna innehåller kommentarer')