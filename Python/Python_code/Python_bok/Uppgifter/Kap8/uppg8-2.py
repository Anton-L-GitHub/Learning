import math
def omkr_area(r):
    return 2 * math.pi * r, math.pi * r**2

r = float(input('Cirkelns radie: '))
o, a = omkr_area(r)
print(f'Omkrets: {o:.3f}')
print(f'Area:    {a:.3f}')