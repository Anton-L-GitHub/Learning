import kortlek
class Spelare():
    def __init__(self, leken, namn = 'Spelaren'):
        self._lek = leken         # referens till kortleken
        self._namn = namn
        self._hand = []
        self._poäng = 0
        self._antal_ess = 0
    def nytt_kort(self):
        k = self._lek.ge()          # dra ett nytt kort
        self._hand.append(k)        # lägg till på handen
        if k.get_valör() == 1:      # Ess?
            self._poäng += 14       # Räkna ess som 14    
            self._antal_ess += 1
        else:
            self._poäng += k.get_valör()
        if self._poäng > 22 and self._antal_ess > 0:
            self._poäng -= 13       # Räkna Ess som 1
            self._antal_ess -= 1
    def korten(self):
        return ', '.join([str(k) for k in self._hand])
    def utskrift(self):
        print(self._namn, 'har:', self.korten(), 
              'och', self._poäng, 'poäng')
class Användare(Spelare):
    def spela(self):
        while True:
            self.nytt_kort()
            self.utskrift()
            if self._poäng >= 21 \
               or not fortsätta('Ett kort till'):
                break
        return self._poäng
class Dator(Spelare):
    def spela(self):
        while self._poäng <= 16:
            self.nytt_kort()
        self.utskrift()
        return self._poäng
def fortsätta(fråga):       # Ställer en fråga
    s = input(fråga + '? ')
    return len(s) > 0 and (s[0] == 'j' or s[0] == 'J') 

# Här börjar exekveringen
print('Välkommen til Tjugoett')
while True:
    lek = kortlek.Kortlek()
    s1 = Användare(lek, 'Spelare 1')
    s2 = Användare(lek, 'Spelare 2')
    print('\nSpelare 1')
    p1 = s1.spela()          # Låt spelare 1 spela
    print('\nSpelare 2')
    p2 = s2.spela()          # Låt spelare 2 spela
    if p1 <= 21 and (p1 > p2 or p2 >21):
        print('Spelare 1 vann') 
    elif p2 <= 21 and (p2 > p1 or p1 > 21):   
        print('Spelare 2 vann')
    else: 
        print('Ingen vann')
    if not fortsätta('\nNytt parti'):
        break