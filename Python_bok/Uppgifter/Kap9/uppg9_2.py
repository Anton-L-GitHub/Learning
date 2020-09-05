import uppg9_1

def fortsätta(fråga):        # ställer en fråga
    s = input(fråga + '? ')
    return len(s) > 0 and (s[0] == 'j' or s[0] == 'J')

while True:
    s1 = uppg9_1.spela()
    print('Spelare 1 fick', s1)
    s2 = uppg9_1.spela()
    print('Spelare 2 fick', s2)
    k = uppg9_1.jämför(s1, s2)
    if k == 0:
        print('Oavgjort')
    else:
        print(f'Spelare {k} vann')
    if not fortsätta('En omgång till'):
        break
