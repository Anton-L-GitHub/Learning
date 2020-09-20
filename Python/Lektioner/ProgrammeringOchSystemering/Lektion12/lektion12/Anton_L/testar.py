def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError()
    for x in range(0, n+1):
        print(x)

print(count_from_zero_to_n(-1))