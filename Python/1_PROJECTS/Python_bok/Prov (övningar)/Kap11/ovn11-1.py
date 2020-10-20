n = input('Filens namn? ' )
with open(n, 'r') as f:
    t = []
    for rad in f:
        t += [float(rad)]
    print(f'Max: {max(t):.1f}, Min: {min(t):.1f}, Medel: {sum(t)/len(t):.1f}') 