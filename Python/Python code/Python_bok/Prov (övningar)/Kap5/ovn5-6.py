t1 = input('Den första texten: ')
t2 = input('Den andra texten: ')
t1 = t1.replace(' ', '').lower()
t2 = t2.replace(' ', '').lower()
anagram = True
for t in t1:
    n1 = 0
    for e in t1:
        if e == t:
            n1 += 1
    n2 = 0
    for e in t2:
        if e == t:
            n2 += 1
    if n1 != n2:
        anagram = False
        break
if anagram:
    print('Anagram')
else:
    print('Inte anagram')   