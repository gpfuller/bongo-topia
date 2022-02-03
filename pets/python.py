class Pet_Owner:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        print(f'{self.pet.name} loves a bath!')
        return self

    def feed(self):
        self.pet.eat()
        print(f'yummmmyyyy {self.pet.name} loves their {self.pet_food}')
        return self
    
    def bathe(self):
        self.pet.noise()
        if self.pet.type != "Dog":
            print(f'*SPLASH* cats hate water')
        else:
            print(f'*SPLASH* all clean!')
        return self

class Pet:
    def __init__(self, name, type, tricks, health = 10, energy = 5):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.energy += 25
        return self

    def noise(self):
        if self.type != "Dog":
            print(f'*SCREAMS*')
        else:
            print(f'{self.name} loves to be clean!')
        return self

joey = Pet("Joey", "Cat", "Stompy")
major = Pet("Major", "Dog", "Fetch")
george = Pet_Owner("George", "Fuller", "Nip", "Raw Fish", joey)
baylee = Pet_Owner("Baylee", "Carroll", "Peanut Butter", "Cooked Steak", major)

george.bathe()


