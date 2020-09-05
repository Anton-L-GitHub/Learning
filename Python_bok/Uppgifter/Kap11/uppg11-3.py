n = input('Filens namn? ')
with open(n, 'r') as f:
    max_tid = 0
    max_användare = ''
    for rad in f:
        ord = rad.split()
        användare = ord[0]
        tider  = [int(e) for e in ord[1:]]
        tid = sum(tider)
        if tid >= max_tid:
            max_tid = tid
            max_användare = användare
    print(max_användare, max_tid)