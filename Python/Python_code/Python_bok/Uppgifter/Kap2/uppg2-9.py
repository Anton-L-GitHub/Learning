# Program som beräknar en cirkels omkrets och area
import math
svar = input('Cirkelns radie: ')
r = float(svar)          # omvandla till float
omkr = 2 * math.pi * r   # beräkna omkretsen
area = math.pi * r**2    # beräkna arean
print(f'Omkrets: {omkr:.3f}')
print(f'Area:    {area:.3f}')