svar = input('Antal sekunder: ')
sek = int(svar)
tim = sek // 3600
sek = sek % 3600
min = sek // 60
sek = sek % 60
print('Timmar:  ', tim)
print('Minuter: ', min)
print('Sekunder:', sek)