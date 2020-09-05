rom = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
rtal = input('Skriv ett romerskt tal: ')
# Ta fram siffrorna i talet
siff = []
for e in rtal:
    r = e.upper()
    if r in rom.keys():
        siff += [rom[r]]
siff += [0]         # Lägg till en extra nolla på slutet

# Beräkna talets värde
sum = 0
for i in range(0, len(siff)-1):
    if siff[i] >= siff[i+1]:
        sum += siff[i]
    else:
        sum -= siff[i]
print('Talets värde är', sum)

