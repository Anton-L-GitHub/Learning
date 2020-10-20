# Mandatfördelning
antalMandat = int(input('Antal mandat? '))
spärr = int(input('Spärr för småpartier. Procent? '))
spärr /= 100       # räkna om från procent
s = input('Antal röster för partierna? ')
röster = [int(x) for x in s.split()]      # antal röster
# Beräkna totala antalet röster
tot = sum(röster)
# Initiera listorna mandat och jfrtal
mandat = [0] * len(röster)           # antal mandat hittills 
jfrtal = []
for i in range(0, len(röster)):
    if röster[i] / tot < spärr:
        röster[i] = 0               # ta bort småpartier
    jfrtal.append(röster[i] / 1.2)  # första jämförelsetal
# Dela ut mandaten
for i in range(0, antalMandat):
    m = max(jfrtal)         # det största jämförelsetalet
    p = jfrtal.index(m)     # har parti nr p
    mandat[p] += 1          # ge mandatet till parti nr p 
    # beräkna ett nytt jämförlsetal för parti nr p 
    jfrtal[p] = röster[p] / (2*mandat[p]+1) 
print('Mandatfördelning:')
print(mandat)