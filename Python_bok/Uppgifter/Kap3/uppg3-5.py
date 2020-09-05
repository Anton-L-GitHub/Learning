l = int(input('Längd (mm)? '))
b = int(input('Bredd (mm)? '))
t = int(input('Tjocklek (mm)? '))
if l >= 140 and l <= 600 and b >= 90 and\
   t <= 100 and b+l+t <= 900 :
    print('Måtten OK')
else: 
    print('Felaktiga mått')   