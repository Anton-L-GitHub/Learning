# Räkna blanka tecken, version 2
s = input('Skriv en text: ')
n = 0
for c in s:
    if c == ' ':
        n = n + 1
print(f'Texten innehåller {n} blanka tecken')