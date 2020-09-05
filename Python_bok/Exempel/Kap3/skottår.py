år = int(input('Skriv ett årtal: '))
if (år % 4 == 0 and år % 100 != 0) or år % 400 == 0:
    print('Skottår')
else:
    print('Inte skottår')