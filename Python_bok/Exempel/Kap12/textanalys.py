# Textanalys
n = input('Filens namn? ')
with open(n, 'r') as f: 
    d = dict()            # en tom avbildningstabell
    bort   = '.,?!:;'     # tecken som ska ersättas med ' '
    t = str.maketrans(bort, ' ' * len(bort))
    for s in f:
        s = s.translate(t)   # ersätt alla specialtecken
        s = s.lower()
        ord = s.split()
        for e in ord:       
            d[e] = d.setdefault(e, 0) + 1  # öka antalet
    for k, v in d.items():
        print(k, v)