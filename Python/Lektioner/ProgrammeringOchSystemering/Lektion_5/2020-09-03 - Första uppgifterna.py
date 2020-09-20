1.
for _ in range(10):
    print('Hello user')

2.
for i in range(1, 10):
    for _ in range(i):
        print(i, end='')
    print('')

3.
while True:
    magic_number = 22
    guess = int(input('Enter a interger: '))
    if guess > magic_number:
        print('Lower!')
    elif guess < magic_number:
        print('Higher!')
    else:
        print('Congratulations, you’re correct!')
        break


4.
numbers = [10, 20, 30, 40, 44, 46, 45, 60]
for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        print(f'[{number}] is not a whole number! ')
        break

5.
first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
list_of_tuples = []
for num_in_second in second_list:
    list_of_tuples.append((first_list.index(num_in_second), num_in_second))
print(list_of_tuples)




6.
first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
list_of_tuples = [(first_list.index(i), i) for i in second_list]
print(list_of_tuples)


7. 
fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
fruits_wanted = int(input('How many fruits does your basket hold: '))
my_basket = []
i = 0
while len(my_basket) <= fruits_wanted:
    if i >= 5:
        i = 0
    my_basket.append(fruits[i])
    i += 1
print(f'My_basket = {my_basket}')


8.
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




