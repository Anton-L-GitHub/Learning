import math
def omkr(r):
    return 2 * math.pi * r
    
def area(r):
    return math.pi * r**2

r = float(input('Cirkelns radie: '))
print(f'Omkrets: {omkr(r):.3f}')
print(f'Area:    {area(r):.3f}')