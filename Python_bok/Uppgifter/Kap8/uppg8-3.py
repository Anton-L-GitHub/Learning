def siff_antal(n):
    sum = 0
    while n > 0:
        n = n // 10           # ta bort den sista siffran
        sum += 1
    return sum