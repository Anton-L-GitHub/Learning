# Modulen kortlek
import random
def ny():                  # skapar en ny, blandad kortlek
    lek = []
    for i in range(1, 5):
        for j in range(1, 14):
            lek.append((i, j))
    random.shuffle(lek)
    return lek
def ge(lek):               # ger det överstakortet i lek
    if len(lek) > 0:
        return lek.pop()
    else:
        return None
färg  = '\N{BLACK CLUB SUIT}\N{WHITE DIAMOND SUIT}'\
        '\N{WHITE HEART SUIT}\N{BLACK SPADE SUIT}'
valör = ('E', '2', '3', '4', '5', '6', '7',
         '8', '9', '10', 'Kn', 'D', 'K')
def visa(k, sist='\n'):             # skriver ut kortet k
    f, v = k
    print(färg[f-1], valör[v-1], end=sist)