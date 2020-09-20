k = int(input('Pris för årskort? '))
b = int(input('Pris för biljett? '))
n = int(input('Antal besök? '))
if n * b <= k:
    print('Köp biljetter')
else:
    print('Köp årskort')