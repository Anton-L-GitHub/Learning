5.
word = input('Skriv ett ord: ')
for i, char in enumerate(word, 1):
    print(word[-i], end='')


8.
for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end=' ')

10.
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        continue
    elif i % 3 == 0:
        print('Fizz')
        continue
    elif i % 5 == 0:
        print('Buzz')
        continue
    else:
        print(i)


11.
result = []
rows = int(input('Rows: '))
columns = int(input('Columns: '))

for i in range(rows):
    temp = []
    for j in range(columns):
        temp.append(i*j)
    result.append(temp)
print(result)

40.
talet = 2
while talet <= 100:
    delat_med = 2
    while delat_med < talet:
        if talet % delat_med == 0:
            break
        delat_med += 1
    else:
        print(talet)
    talet += 1

