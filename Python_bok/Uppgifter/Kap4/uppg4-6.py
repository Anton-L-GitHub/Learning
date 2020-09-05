n = int(input('Talet n? '))
sum = 0
for i in range(1, n+1):
    sum = sum + i*i
    i= i + 1
print('Summan =', sum)