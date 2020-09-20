svar = input('Pris (inkl. moms): ')
p = float(svar)
svar = input('Procent moms: ')
m = float(svar)
exkl = p / (1 + m/100)
moms = exkl * m/100
print(f'Pris:{exkl:6.2f}')
print(f'Moms:{moms:6.2f}')