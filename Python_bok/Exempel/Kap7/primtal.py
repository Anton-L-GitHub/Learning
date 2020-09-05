# Primtal
while True:
    # Läs in ett tal och avbryt om användaren vill sluta
    s = input('Talet? ')
    if s == '':
        break
    talet = int(s)
    # Undersök om talet är ett primtal
    är_primtal = True
    for k in range(2, talet):
        if talet % k == 0:
            är_primtal = False
    # Skriv ut resultatet
    if är_primtal:
        print('Primtal')
    else:
        print('Ej primtal') 