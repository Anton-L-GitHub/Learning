# Version 1
def är_udda(k):
    return k % 2 == 1

s = input('Skriv ett antal heltal: ')
tal = [int(e) for e in s.split()]
udda_tal = list(filter(är_udda, tal))
print(udda_tal)

# Version 2
s = input('Skriv ett antal heltal: ')
tal = [int(e) for e in s.split()]
udda_tal = list(filter(lambda k : k % 2 == 1, tal))
print(udda_tal)