# Beräkning av summan 1+2+3+ .. +n 
n = int(input('n? '))
summa = 0
k = 1
while k <= n:
    summa = summa + k      # öka summan med k
    k = k + 1              # öka k med 1
print('Summan blir', summa)