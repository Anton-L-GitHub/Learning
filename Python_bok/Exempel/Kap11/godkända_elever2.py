# Godkända elever, version 2
n1 = input('Filen med resultat? ')
n2 = input('Filen med godkända? ')
with open(n1, 'r') as f1, open(n2, 'w') as f2: 
    for rad in f1:
        ord = rad.split()
        namnen = [e for e in ord if not e.isdecimal()]
        poäng  = [int(e) for e in ord if e.isdecimal()]
        namn = ' '.join(namnen) 
        summan = sum(poäng)
        if summan >= 50:
            print(namn, summan, file=f2)