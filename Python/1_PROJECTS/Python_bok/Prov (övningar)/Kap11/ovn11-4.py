n1 = input('Infilens namn? ' )
n2 = input('Utfilens namn? ')
with open(n1, 'r') as f1, open(n2, 'w') as f2:
    while True:
        rad1 = f1.readline()
        if rad1 =='':
            break
        rad2 = f1.readline()
        data = rad2.split()
        längd = int(data[1])
        vikt = float(data[2])
        bmi = vikt / (0.01*längd) ** 2
        if bmi > 30:
            f2.write(rad1)
            f2.write(rad2)