class Pet:
    def __init__(self, name, tricks, kind):
        self.name = name
        self.tricks = tricks
        self.kind = kind
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 10


class Cat(Pet):
    def __init__(self, name, tricks, kind = "Cat"):
        super().__init__(name, tricks, kind)
        self.kind = kind
        self.health = 900
        self.energy = 150
    # noise() - prints out the pet's sound
    def noise(self):
        print("Mrrrr!")

class Dog(Pet):
    def __init__(self, name, tricks, kind = "Dog"):
        super().__init__(self, name, tricks)
        self.kind = kind
        self.health = 100
        self.energy = 300
    # noise() - prints out the pet's sound
    def noise(self):
        print("Awoof!")
