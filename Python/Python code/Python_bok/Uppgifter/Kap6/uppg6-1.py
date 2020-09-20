n = int(input('Antal tal? '))
k = 3
f = [2]
for i in range(1, n): 
  f += [f[i-1] * k]
print(f)