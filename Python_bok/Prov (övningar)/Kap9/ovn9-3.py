def jfr(k):
    f, v = k
    if v == 1:
        v = 14
    return f * 14 + v

# Testprogrammet   
from kortlek import *
b = ny()
while len(b) > 0:
    k1 = ge(b)
    k2 = ge(b)
    if jfr(k1) > jfr(k2):
        störst, minst = k1, k2
    else: 
        störst, minst = k2, k1
    visa(störst, ' ')
    print('är högre än ', end='')
    visa(minst)