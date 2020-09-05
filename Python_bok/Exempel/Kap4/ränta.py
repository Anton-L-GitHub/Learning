# Ränteberäkning
ränta = float(input('Räntesats? '))
n = int(input('Antal år? '))
kapital = 1000
for år in range(1, n+1, 1):
    kapital = kapital + kapital * 0.01 * ränta
    print(f'{år:3}{kapital:6.0f}')