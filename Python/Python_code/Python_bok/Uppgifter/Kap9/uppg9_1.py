import random

def spela():
    ord = ['Sten', 'Sax', 'Påse']
    return ord[random.randint(0, 2)]

def jämför(ord1, ord2):
    if ord1 == ord2:
        return 0      # Betyder oavgjort
    elif ord1 == 'Sten' and ord2 == 'Sax'  or \
         ord1 == 'Sax'  and ord2 == 'Påse' or \
         ord1 == 'Påse' and ord2 == 'Sten':
        return 1
    else:
        return 2

