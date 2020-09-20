#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Dog:
    
    super_friendly = "golden retriever"

    def __init__(self, name, age, owner, breed):
        self.name = name
        self.age = age
        self.owner = owner
        self.breed = breed
        self.best_friend = []

    def set_name(self, name):
        self.name = name     
    
    def set_age(self, age):
        self.age = age

    def set_owner(self, owner):
        self.owner = owner

    def set_breed(self, breed):
        self.breed = breed

    def set_favorite_toy(self, favorite_toy):
        self.favorite_toy = favorite_toy

    def add_best_friend(self, name):
        
        if self.best_friend ==[]:
            self.best_friend.append(name)

        elif self.best_friend == name: #den vännen är redan tillagd
            pass 
        
        elif self.breed == self.super_friendly:  #finns det risker här?
            self.best_friend.append(name)
        
        else:
            print("Enbart möjligt med en bästa vän, förutom för goldens")


# In[7]:


class Dog_daycare():
    
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
        self.list_of_dogs = []
    
    def add_dog(self, name, age, owner, breed):
        temp_dog = Dog(name, int(age), owner, breed)
        self.list_of_dogs.append(temp_dog)

    def remove_dog(self, name):
        for i, dog in enumerate(self.list_of_dogs):
            if dog.name == name:
                del self.list_of_dogs[i] #varför är det viktigt med self.list här?
                break
                
    def set_manager(self, name):
        self.manager = name


# In[8]:


def menu(daycare):
    print_choices()
    choice = 0
        
    while choice != 9:
                
        choice=int(input("\nGör ditt val: "))
    
        if choice == 1:
            print("Vänligen skriv namn, ålder, ägare och hundras för hunden")
            name = input("Namn: ")
            age = input("Ålder: ")
            owner = input("Ägare: ")
            breed = input("Hundras ")
            
            daycare.add_dog(name, age, owner, breed)
    
        elif choice == 2:
            name = str(input("Vänligen skriv namnet på hunden du vill ta bort från dagiset: "))
            daycare.remove_dog(name)
        
        elif choice == 3:
            
            name = input("Vänligen skriv in nuvarande hundnamnet: ")
            new_name = input("Skriv in nya hundnamnet: ")
            
            for dog in daycare.list_of_dogs: #kan det uppstå problem med denna implementation? om ja, vilka? 
                if dog.name == name:
                    dog.set_name(new_name)
        
        elif choice == 4:

            owner = input("Skriv in namnet på den gamla ägaren: ")
            new_owner = input("Skriv in namnet på nya ägaren: ")
            
            for dog in daycare.list_of_dogs:
                if dog.owner == owner:
                    dog.set_owner(new_owner)
        
        elif choice == 5:
            print(f"Chefens namn är: {daycare.manager}")
            name = input("Skriv in nya chefens namn ")
            
            daycare.set_manager(name)
            print(f"Har nu bytt chef till {daycare.manager}")
        
        elif choice == 6:
            for dog in daycare.list_of_dogs:
                print(f"Namn: {dog.name }, Ålder: {dog.age}, Ägare: {dog.owner}, Bästa vän: {dog.best_friend}")

                if(hasattr(dog, 'favorite_toy')): 
                    print(f" Favoritleksak: {dog.favorite_toy}")

        elif choice == 7:
            dog_getting_a_friend = input("Vänligen skriv in hunden som ska få en bästa kompis ")
            dog_friend = input("Vänligen skriv in namnet på bästa hundkompisen ")

            
            for dog in daycare.list_of_dogs: 
                if dog.name == dog_getting_a_friend:
                    dog.add_best_friend(dog_friend) #bara ett namn här! kan egentligen skriva in hundnamn som inte finns hos dagiset
       
        elif choice == 8:
            dog_name = input("Vänligen skriv namnet på hunden som ska få en favoritleksak")
            toy = input("Vänligen skriv vilken leksak hunden har som favorit ")

            for dog in daycare.list_of_dogs: 
                if dog.name == dog_name:
                    dog.set_favorite_toy(toy)

        elif choice == 9:
            exit()    
        
        else:
            print("\n- Ogiltigt alternativ. Välj något mellan 1 och 9")
            
        print_choices()


# In[9]:


def print_choices():
    print("\n Välj mellan följande alternativ: \n 1. Lägg till hund till dagis \n 2. Ta bort en hund från dagiset     \n 3. Ändra namnet på en hund \n 4. Byt ägare på en hund \n 5. Byt chef på dagiset.    \n 6. Lista alla hundar vid dagiset     \n 7. Lägg till bästa kompis för en hund \n 8. Lägg till favoritleksak för en hund \n 9. Avsluta")


# In[ ]:


vacker_tass = Dog_daycare("Vacker Tass", "Jenny")
vacker_tass.add_dog("Fido", 2, "Maria", "tax")
vacker_tass.add_dog("Rocky", 3, "Maria", "pudel")
vacker_tass.add_dog("Aleksa", 3, "Sara", "golden retriever")

menu(vacker_tass)


# In[ ]:




