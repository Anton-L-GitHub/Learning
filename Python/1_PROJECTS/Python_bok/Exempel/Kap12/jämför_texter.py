# Jämför texter
def skapa_ordmängd(f):    # hjälpfunktion
    m = set()             # en tom mängd
    bort   = '.,?!:;'     # tecken som ska ersättas med ' '
    for s in f:
        for c in bort:
            s = s.replace(c, ' ')    
        s = s.lower()
        ord = s.split()   # skapa en lista med ord på raden
        m = m | set(ord)  # utöka mängden
    return m
# Här börjar exekveringen
n1 = input('Den första filens namn? ')
n2 = input('Den andra filens namn? ')
with open(n1, 'r') as f1, open(n2, 'r') as f2: 
    m1 = skapa_ordmängd(f1)     # orden i första filen
    m2 = skapa_ordmängd(f2)     # orden i andra filen
    m = m1 & m2                 # gemensamma ord
    print(m)