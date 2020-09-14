class Dog_daycare:
    def __init__(self, name, boss):
        self._name = name
        self._boss = boss
        self._dogs = []

    def add_dog(self, name, age, owner, breed):
        dog = Dog(name, age, owner, breed)
        self._dogs.append(dog)

    def remove_dog(self, dog_id):  # Add more identifiers
        for dog in self._dogs:
            if dog._id == dog_id:
                self._dogs.remove(dog)

    def set_boss_name(self):
        pass

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
        name = self._name

    def set_age(self, age):
        # assert age >
        age = self._age

    def set_owner(self, owner):
        owner = self._owner

    def set_breed_toy(self, breed, favourite_toy):
        pass

    def add_best_friend(self, best_friend):
        if len(self._bf) >= 1:
            if best_friend._breed == 'Golden Retriever':
                self._bf.append(best_friend)
            else:
                return 'Mer vänner?! Skulle inte tro det!'
        else:
            # Får max vara en annan hund OM INTE bf är en golden retriever
            pass

    def __repr__(self):
        return f'ID = {self._id}    | {self._name} - {self._age}år - {self._owner} - {self._breed}'



MENU = """\n\n-------------------------------------------------
0. Avsluta
1. Lägg till hund
2. Ta bort hund
3. Ändra hundens namn
4. Ändra hundägare
5. Visa alla hundar
--ADMIN--
6. Ändra chefen för dagiset

 
Skriv in siffran på vad du vill göra:
> """



if __name__ == '__main__': # Gör till main funktion och sätt att den skall köras ifall name == main
    from time import sleep
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
            pass
        elif user_input == '4':
            pass
        elif user_input == '5':
            for hund in hunddagis.list_dogs():
                print(hund)
        elif user_input == '6':
            pass
        elif user_input == '7':
            pass
        elif user_input == '8':
            pass
        else:
            print('Ej ett kommand. Försök igen!')
        input('')
