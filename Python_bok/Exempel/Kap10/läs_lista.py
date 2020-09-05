def läs_lista():
    print('Skriv ett tal per rad. Avsluta med en tom rad.') 
    v = []
    while True:
        s = input('> ')
        if s == '':
            return v         # listan klar
        try:
            x = float(s)
            v.append(x)      # talet OK, lägg till listan
        except ValueError:
            print('Felaktigt tal:', s, 'Försök igen')