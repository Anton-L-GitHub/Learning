konsonanter = 'bcdfghjklmnpqrstvxz'
namn = input('Filens namn? ' )
with open(namn, 'r') as f:
    for s in f:
        i = 0
        while i < len(s):
            print(s[i], end='')
            t = s[i].lower()
            if t in konsonanter:
                i += 3
            else:
                i += 1