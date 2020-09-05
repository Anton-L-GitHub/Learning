with open('personer.txt', 'a') as f:
    print('Skriv namn. Avsluta med en tom rad')
    while True:
        rad = input('> ')
        if rad == '':
            break
        f.write(rad + '\n')