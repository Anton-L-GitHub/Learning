# Fibonacci
n = int(input('Hur många tal önskas? ')) 
f = [0, 1]
for i in range(2, n+1):
    f += [f[i-2] + f[i-1]]   # lägg till nästa tal
print(f)                     # skriv ut alla talen