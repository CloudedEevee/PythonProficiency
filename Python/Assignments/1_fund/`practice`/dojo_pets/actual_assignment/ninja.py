import pet

class Ninja:
    def __init__( self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    
# implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        pet.Pet.play(self.pet)
        print(f"You took {self.pet.name} for a walk! +10 Health")
        return self


    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        pet.Pet.eat(self.pet)
        print(f"You fed {self.pet.name}! +5 Energy   +10 Health")
        return self    


    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        pet.Pet.noise(self.pet)
        print(f"Oh! Looks like {self.pet.name} is happy that they're clean!")