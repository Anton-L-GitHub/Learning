def läs_tal():
    while True:
        try:
            s = input('Skriv ett tal: ')
            x = float(s)
            return x
        except ValueError:
            print('Felaktigt tal:', s, 'Försök igen')