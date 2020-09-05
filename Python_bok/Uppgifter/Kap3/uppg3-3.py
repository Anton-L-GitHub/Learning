poäng = int(input('Antal poäng? '))
if poäng >= 45:
    betyg = 'A'
elif poäng >= 40:
    betyg = 'B'
elif poäng >= 35:
    betyg = 'C'
elif poäng >= 30:
    betyg = 'D'
elif poäng >= 25:
    betyg = 'E'
else:
    betyg = 'F'
print('Betyg:', betyg)