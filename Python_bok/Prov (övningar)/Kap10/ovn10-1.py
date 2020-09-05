def fyll(a, i1, i2, v):
    assert i1 >= 0 and i2 < len(a) and i1 <= i2 
    a[i1:i2+1] = [v] * (i2+1-i1)

# Test
l = [1, 2, 3, 4, 5]
fyll(l, 4, 2, 99)