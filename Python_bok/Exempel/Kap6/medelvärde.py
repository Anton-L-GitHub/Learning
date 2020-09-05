# Beräkna medelvärde, version 2
s = input('Skriv ett antal tal: ')
ls = s.split()
talen = [float(t) for t in ls]
medel = sum(talen) / len(talen)
print(f'Medelvärdet är {medel:1.2f}')