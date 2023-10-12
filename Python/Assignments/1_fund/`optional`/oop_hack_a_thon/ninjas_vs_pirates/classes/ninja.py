import random

class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 7
        self.speed = 6
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
    
    def can_attack(self, pirate):
        can_attack = False
        atk_roll = random.randint(0, 20) + self.speed
        def_roll = random.randint(0, 20) + pirate.speed
        if atk_roll > def_roll:
            can_attack = True
        return can_attack

    def is_crit(self):
        is_crit = False
        random_int = random.randint(0, (20-self.speed))
        if random_int == 0:
            is_crit = True
        return is_crit

    def attack (self, pirate):
        if Ninja.can_attack(self, pirate):
            if Ninja.is_crit(self):
                print(f"Crit!!! {self.strength * 2} dmg")
                pirate.health -= self.strength * 2
            pirate.health -= self.strength
        else:
            print("Miss!")
        return self