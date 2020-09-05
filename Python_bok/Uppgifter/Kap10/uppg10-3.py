s = input('Skriv ett tal: ')
for e in s:
    if e < '0' or e > '9':
        print('Inget tal')
        break
else:
    print('Talet är OK')