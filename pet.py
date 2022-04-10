class Pet:
    # implement __init__( name , type , tricks ):
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound

    # class attributes
    pet_health = 100
    pet_energy = 100

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.pet_noise = f"{self.type} noise"

    def sleep(self):
        self.pet_energy += 25
        print(f"{self.name}'s energy is now at: {self.pet_energy}")

    def eat(self):
        self.pet_energy += 5
        self.pet_health += 10
        print(f"{self.name}'s energy is now at: {self.pet_energy}")
        print(f"{self.name}'s health is now at: {self.pet_health}")

    def play(self):
        self.pet_health += 5
        print(f"{self.name}'s health is now at: {self.pet_health}")

    def noise(self):
        print(f"{self.name} makes a {self.pet_noise} at you")

#     @classmethod
#     def print_health(cls, pet_health):
#         print(f"pet health is now at: {pet_health}")
    
#     @classmethod
#     def print_energy(cls, pet_energy):
#         print(f"pet energy is now at: {pet_energy}")

# # subclass
# class Dog( Pet ):
#     def __init__(self, name, type, tricks):
#         super().__init__(name, type, tricks)
    
#     def noise(self):
#         print(f"{self.name} barks at you")