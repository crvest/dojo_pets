from unicodedata import name
from pet import Pet

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )


    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Spot", "dog", "sit")

    def walk(self):
        print(f"{self.first_name} takes their pet for a walk")
        self.pet.play()

    def feed(self):
        print(f"{self.first_name} feeds their pet {self.pet.type} some {self.pet_food}")
        self.pet.eat()

    def bathe(self):
        print(f"{self.first_name} gives their pet {self.pet.type} a bathe")
        self.pet.noise()

hattori = Ninja("Hanzo", "Hattori", "cookies", "purina", Pet("Fido", "Bulldog", "speak"))
hattori.pet = Pet("Fido", "Bulldog", "speak")
print("--------")
hattori.walk()
print("--------")
hattori.feed()
print("--------")
hattori.bathe()
print("--------")