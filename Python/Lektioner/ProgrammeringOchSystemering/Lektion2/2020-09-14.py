class Dog_daycare:
    def __init__(self, name, boss):
        self._name = name
        self._boss = boss
        self._dogs = []

    def add_dog(self, name, age, owner, breed):
        dog = Dog(name, age, owner, breed)
        self._dogs.append(dog)

    def remove_dog(self, dog_id):
        for dog in self._dogs:
            if str(dog._id) == dog_id:
                self._dogs.remove(dog)

    def set_boss_name(self, boss):
        self._boss = boss

    def list_dogs(self):
        doglist = [dog for dog in self._dogs]
        return doglist
        

    def __str__(self):
        return self._name


class Dog:
    id = 1

    def __init__(self, name, age, owner, breed):
        self._id = Dog.id
        self._name = name
        self._age = age
        self._owner = owner
        self._breed = breed
        self._bf = []
        Dog.id += 1

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        # assert age >
        self._age = age

    def set_owner(self, owner):
        self._owner = owner

    def set_breed_toy(self, breed, favourite_toy):
        pass

    def add_best_friend(self, dog, best_friend):
        if len(self._bf) >= 1:
            if best_friend._breed == 'Golden Retriever':
                self._bf.append(best_friend)
            else:
                return 'Mer vänner?! Skulle inte tro det!'
        else:
            # Får max vara en annan hund OM INTE bf är en golden retriever
            pass

    def __str__(self):
        return f'ID= {self._id}| Hund: {self._name}\t{self._age}år {self._owner}\t{self._breed}'

    def __repr__(self):
        return self




MENU = """\n\n-------------------------------------------------
0. Avsluta
1. Lägg till hund
2. Ta bort hund
3. Ändra hundens namn
4. Ändra hundägare
5. Visa alla hundar
6. Lägg till Hundens BFF
--ADMIN--
9. Ändra chefen för dagiset

 
Skriv in siffran på vad du vill göra:
> """


if __name__ == '__main__':  # Gör till main funktion och sätt att den skall köras ifall name == main
    hunddagis = Dog_daycare('Vacker Tass', 'Stefan Löfven')
    while True:
        user_input = input(MENU)
        if user_input == '0':
            print('Avslutar.. Cya later m8!')
            break
        elif user_input == '1':
            print('\nAnge hundens..')
            namn = input('Namn: ').title()
            age = input('Ålder: ')
            owner = input('Ägare: ').capitalize()
            breed = input('Ras: ').capitalize()
            hunddagis.add_dog(namn, age, owner, breed)
        elif user_input == '2':
            dog_id = input('Ta bort hund\nHundens ID: ')
            hunddagis.remove_dog(dog_id)
        elif user_input == '3':
            dog_input = int(input('Ändra hundens namn\nHundens ID: '))
            for dog in hunddagis.list_dogs():
                if dog._id == dog_input:
                    hunddagis._dogs.remove(dog)
                    new_name = input(f'Nytt namn {dog._name}: ')
                    dog.set_name(new_name)
                    hunddagis._dogs.append(dog)
        elif user_input == '4':
            owner_input = int(input('Ändra hundens ägare\nHundens ID: '))
            for dog in hunddagis.list_dogs():
                if dog._id == owner_input:
                    hunddagis._dogs.remove(dog)
                    new_owner = input(f'Ny ägare till {dog._name}: ')
                    dog.set_owner(new_owner)
                    hunddagis._dogs.append(dog)
        elif user_input == '5':
            for hund in hunddagis.list_dogs():
                print(hund)
        elif user_input == '6':
            dogg_bff = input('Vilken liten rackare har fått en ny kompis?')
            for dog in hunddagis.list_dogs():
                if dog._id == owner_input:
                    hunddagis._dogs.remove(dog)
                    new_owner = input(f'Ny ägare till {dog._name}: ')
                    dog.set_owner(new_owner)
        elif user_input == '7':
            pass
        elif user_input == '9':
            new_boss = input('Namn på ny chef: ')
            hunddagis.set_boss_name(new_boss)
        else:
            print('Ej ett kommand. Försök igen!')
        input('')
