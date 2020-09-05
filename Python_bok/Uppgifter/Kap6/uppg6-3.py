import random
t = list()
sum = 0
for i in range(0, 100):
    x = random.randint(1,1000)
    sum += x
    t.append(x)
print(f'Minsta tal: {min(t):d}')
print(f'Största tal: {max(t):d}')
print(f'Medelvärde: {sum/len(t):1.2f}')