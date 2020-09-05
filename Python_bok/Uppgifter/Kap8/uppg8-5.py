def är_perfekt(n):
  sum = 0
  for k in range(1, n):
    if n % k == 0:
      sum = sum + k
  return sum == n

tal = int(input('Skriv ett tal: '))
if är_perfekt(tal):
    print('Talet är perfekt')
else:
    print('Talet är inte perfekt')   