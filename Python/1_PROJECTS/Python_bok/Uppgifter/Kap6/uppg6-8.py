# Skapa multiplikationstabell
n = int(input('Tabellens storlek? '))
a = []
for i in range(0, n):
    a.append([])
    for j in range(0, i+1):
        a[i].append((i+1) * (j+1))
for i in range(0, n):
    for j in range(0, i+1):
        print(f'{a[i][j]:3d}', end='')
    print() 