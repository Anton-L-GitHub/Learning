from sys import argv
for fil in argv[1:]:
    with open(fil, 'r') as f:
        r= 0      # antal rader och tecken
        for rad in f:
            r += 1
    print(f'{fil:s}: {r} rader') 