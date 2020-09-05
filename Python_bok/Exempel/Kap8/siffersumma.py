# Siffersumman
def siff_sum(n):
    sum = 0
    while n > 0:
        rest = n % 10
        sum = sum + rest      # addera sista siffran
        n = n // 10           # ta bort den sista siffran
    return sum