def fyll(a, i1, i2, v):
    a[i1:i2+1] = [v] * (i2+1-i1)
