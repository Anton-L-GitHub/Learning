def nfak(n):
    r = 1
    for i in range(2, n+1):
        r = r * i
    return r

print(nfak(4))