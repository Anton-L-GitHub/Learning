import math
svar = input('Cirkelns radie: ')
r = float(svar)
omkr = 2 * math.pi * r
area = math.pi * r**2
print(f'Omkrets: {omkr:.3f}')
print(f'Area:    {area:.3f}')