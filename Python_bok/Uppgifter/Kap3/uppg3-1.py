m = int(input('Antal minuter? '))
p = float(input('Pris per minut? '))
t = m * p
if t >= 300:
	 t = t * 0.9 
print(f'Det kostar {t:.2f} kr')