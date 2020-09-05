1. 12
2. 22
3. 10
4. 5
5. print('Hello World')

6. 
a = float(input('Ange tal A: '))
b = float(input('Ange tal B: '))
print(f'\nSumman av talen = {a+b:.0f} \nSkillnaden mellan talen = {abs(a-b):.0f} \nProdukten av talen = {a*b:.0f}')

7.
a = float(input('Ange tal A: '))
b = float(input('Ange tal B: '))
print(f'Divition = {a/b} | Floor = {a//b}')

8.
import math
radie = float(input('Cirkelns radie: '))
area = radie**2 * math.pi
print(f'Area = {area:.3f}')

9.
bas = float(input('Bas: '))
hojd = float(input('Hojd: '))
area = bas * hojd / 2
print(f'Area = {area}')

10.
def ekvation(x, y):
    return (x + y) * (x + y)


x = float(input('X: '))
y = float(input('Y: '))
print(f'({x}+{y})*({x}+{y}) = {ekvation(x, y)}')


11.
import math
a = float(input('Ange sida a: '))
b = float(input('Ange sida b: '))

print(f'Hypotenusan = {math.sqrt(a**2+b**2)}')

12.
minuter = 455
h = minuter//60
m = minuter % 60
print(f'Timmar = {h}\nMinuter = {m}')

13.
s = int(input('Sekunder: '))
m = s / 60
h = s / 3_600
d = s / 86_400
print(f'Sekunder    =   {s} \n'
      f'Minuter     =   {m} \n'
      f'Dagar       =   {d} \n')

14.

a = 'Hej'
b = 'Då'
print(a, b)
c = a
a = b
b = c
print(a, b)

--
a = 'Hej'
b = 'Då'
print(a, b)
a, b = b, a
print(a, b)


15. 
x = y = z = 'Hej'
print(x, y, z)

16.
c = float(input('Ange temperatur (C): '))
f = c * 9/5 + 32
print(f'Celsius     =   {c}\n'
      f'Fahrenheit  =   {f}')

17.
- Onödiga kommentarer
- Onödiga variabler
- Dåligt namn på variabel


