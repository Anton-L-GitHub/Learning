def nfak(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * nfak(n-1)

while True:
    n = int(input('n? '))
    print(nfak(n))