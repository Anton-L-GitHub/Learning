# Kontantkort, lägsta pris
namn = []
pris = []
while True:
    s = input('Namn och pris för ett kort: ')
    if s == '':
        break
    s = s.strip()      # ta bort ev. blanka först och sist
    i = s.rfind(' ')             # sök index före priset
    namn.append(s[0:i])          # bilda skiva med namnet
    pris.append(float(s[i+1:]))  # bilda skiva med priset
m = min(pris)                    # sök lägsta pris
k = pris.index(m)                # index för lägsta pris
print(namn[k] + ' är billigast')
print(f'Kostnad: {m:1.2f} kr/månad')