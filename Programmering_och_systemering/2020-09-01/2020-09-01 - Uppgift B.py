p1_name = input("Please enter name for person 1\n>").capitalize()
p1_age = input("Please enter age for person 1 \n>")
p1_shoe = input("Please enter shoe size for person 1 \n>")

p2_name = input("Please enter name for person 2\n>").capitalize()
p2_age = input("Please enter age for person 2 \n>")
p2_shoe = input("Please enter shoe size for person 2 \n>")

p3_name = input("Please enter name for person 3\n>").capitalize()
p3_age = input("Please enter age for person 3 \n>")
p3_shoe = input("Please enter shoe size for person 3 \n>")

p_all = [
    {"name": p1_name, "age": p1_age, "shoe size": p1_shoe},
    {"name": p2_name, "age": p2_age, "shoe size": p2_shoe},
    {"name": p3_name, "age": p3_age, "shoe size": p3_shoe},
]

oldest = sorted(p_all, key=lambda age: age["age"])[-1]
median_size = sorted(p_all, key=lambda size: size["shoe size"])[1]

print(
    f"The oldest person is [{oldest['name']}] "
    f"who has shoe size [{oldest['shoe size']}]"
)

print(
    f"The person with the median shoe size is [{median_size['name']}] "
    f"who is [{median_size['age']}]"
)

search_key = input("> ").split()
search_p = next(filter(lambda i: i[search_key[0]] == search_key[1], p_all))
print(
    f"\nFound person! \n"
    f"Name: {search_p['name']}\n"
    f"Age: {search_p['age']} \n"
    f"Size: {search_p['shoe size']}"
)
