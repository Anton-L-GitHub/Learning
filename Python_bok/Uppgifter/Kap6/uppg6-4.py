s = input('Skriv en lista med heltal: ')
ls = s.split()
talen = list(map(int, ls))
for i in range(0, talen.count(0)):
    talen.remove(0)
print(talen)