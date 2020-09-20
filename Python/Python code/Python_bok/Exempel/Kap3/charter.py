pris = float(input('Grundpris? '))
ålder = int(input('Ålder? '))
if ålder < 12:
    pris = pris * 0.5
elif ålder >= 65:
    pris = pris * 0.75
else:
    pris = pris * 0.9
print(f'Pris: {pris:.2f} kr')