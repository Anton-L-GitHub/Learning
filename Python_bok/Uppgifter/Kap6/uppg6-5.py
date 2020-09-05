# Kontantkort, lägsta pris
namn = []
pris = []
while True:
    s = input('Namn och pris för ett kort: ')
    if s == '':
        break
    s = s.strip()      # ta bort ev. blanka först och sist
    t = s.rpartition(' ')        # ger (namn, ' ', pris)
    namn.append(t[0])            # lägg till namnet
    pris.append(float(t[2]))     # lägg till priset
m = min(pris)                    # sök lägsta pris
k = pris.index(m)                # index för lägsta pris
print(namn[k] + ' är billigast')
print(f'Kostnad: {m:1.2f} kr/månad')