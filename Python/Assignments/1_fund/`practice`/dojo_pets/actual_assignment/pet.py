class Pet:
    def __init__(self, name, kind, tricks):
        self.name = name
        self.kind = kind
        self.tricks = tricks
        self.health = 100
        self.energy = 150



# implement the following methods:
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
    # noise() - prints out the pet's sound
    def noise(self):
        print("RAWWWWWRRR!!")
