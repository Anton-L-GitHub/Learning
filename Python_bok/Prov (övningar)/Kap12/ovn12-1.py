morse = ['.-',    '-...',  '-.-.', '-..',  '.',    '..-.',
        '--.',   '....',  '..',   '.---', '-.-',  '.-..',
        '--',    '-.',    '---',  '.--.', '--.-', '.-.',
        '...',   '-',    '..-',  '...-', '.--',  '-..-',
        '-.--',  '--..',  '.--.-','.-.-', '---.']
alfabet = 'a b c d e f g h i j k l m n o p q r s t u v x y z å ä ö'.split()

# Del 1
tab1 = dict(zip(alfabet, morse))
m1 = input('Skriv ett meddelande: ')
print('Som morsekod:')
for e in m1:
    t = e.lower()
    kod = tab1.get(t, ' ')
    print(kod, end=' ')
print()

# Del 2
tab2 = dict(zip(morse, alfabet))
m2 = input('Skriv ett meddelande i morsekod: ').split()
print('I klartext:')
for e in m2:
    bokstav = tab2.get(e, '?')
    print(bokstav, end=' ')


