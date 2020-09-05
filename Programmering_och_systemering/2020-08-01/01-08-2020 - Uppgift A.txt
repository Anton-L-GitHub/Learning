1. int

2. dict

3. addresses['Bella']

4. Daniel och hans address läggs till

5. print(len(addresses))

5.1
personer = sorted(list(addresses.keys()))
print(addresses[personer[-1]])

5.2
name_last = sorted(list(addresses.values()))[0]
name_adrs = [name for name, adrs in addresses.items() if adrs == name_last]
print(*name_adrs)

6.
list

7.
Opel

8.
Error, listan har EJ 4st element

9.
BMV

10.
Båda listorna har uppdaterats.

10.1
cars3 = cars.copy()

10.2
cars = sorted([car for car in cars] * 2)
cars.reverse()
print(cars)

10.3
unique_cars = list(set(cars))
print(unique_cars)

11.
set

12.
alla värden är: int

13.
2, 3

14.
1, 2, 3, 4, 6, 7

15.
1, 4, 6, 7

