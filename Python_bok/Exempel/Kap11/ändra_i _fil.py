from namnet import namnet
try:
    # Steg 1
    print('Avsluta med Ctrl-c')
    f_namn = input('Filen med resultat? ')
    with open(f_namn, 'r') as f:  
        rader = f.readlines()        # läs in hela filen  
    # Steg 2
    while True:
        ny_rad = input('> ') + '\n' 
        nytt_namn = namnet(ny_rad)
        if nytt_namn == '':
            print('Felaktig rad')
            continue                 # hoppa över 
        inlagd = False
        for i in range(0, len(rader)):
            namn_i = namnet(rader[i])
            if nytt_namn == namn_i:
                rader[i] = ny_rad    # ändra denna rad
                inlagd = True
                break
        if not inlagd:
            rader.append(ny_rad)     # namnet fanns inte
except KeyboardInterrupt:
    # Steg 3
    with open(f_namn, 'w') as f:
        for rad in rader:
            f.write(rad)