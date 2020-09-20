# Tjugoett
import kortlek
def spela(lek, spelare):    # En av spelarna spelar
    p = 0
    hand = []
    while True:
        k = kortlek.ge(lek)
        hand.append(k)
        p = poäng(hand)
        print(spelare, 'fick ', end = '')
        kortlek.visa(k, '')
        print(f' och har {p} poäng')
        if spelare == 'Du' and\
           (p >=21 or not fortsätta('Ett kort till')) or\
           spelare == 'Datorn' and p >= 17:
           break
    return p
def poäng(hand):            # Beräknar poängen för en hand
    p, antal_ess = 0, 0
    for k in hand:
        if k[1] == 1:       # Ess?
            p += 14         # Räkna ess som 14    
            antal_ess += 1
        else:
            p += k[1]
    while p > 21 and antal_ess > 0:
        p -= 13             # Räkna Ess som 1
        antal_ess -= 1 
    return p
def fortsätta(fråga):       # Ställer en fråga
    s = input(fråga + '? ')
    return len(s) > 0 and (s[0] == 'j' or s[0] == 'J')
# Här börjar exekveringen
print('Välkommen til Tjugoett')
while True:
    lek = kortlek.ny()
    p1 = spela(lek, 'Du')           # Låt användaren spela
    if p1 > 21:
        print('Du förlorade')
    elif p1 == 21:
        print('Du vann') 
    else: 
        p2 = spela(lek, 'Datorn')   # Låt datorn spela
        if p2 <= 21 and p2 >= p1:
            print('Du förlorade')
        else:    
            print('Du vann') 
    if not fortsätta('Nytt parti'):
        break