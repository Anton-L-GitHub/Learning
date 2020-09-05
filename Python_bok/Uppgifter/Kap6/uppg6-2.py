s = input('Skriv ett antal tal: ')
ls = s.split()
talen = [int(t) for t in ls]
negativa = [t for t in talen if t < 0]
print('Antal tal mindre än noll:', len(negativa))