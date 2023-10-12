# Create a Class
class Person:
    def __init__(self, first_name, last_name, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation

    # Can have additional class methods to access
    def walk(self):
        print("Walking...")

    def run(self):
        print("Running...")


# Create a Class Instance
user = Person("Twilight", "Sparkle", "Princess of Magic")


# Use the class instances / class methods
    # Instance attributes
print(user.first_name)
    # Class methods
user.walk()
user.run()








# ##### NOTES ##### #
    # `print(user)` -> results = `<__main__.Person object at 0x7f546354ffd0>`
    # `print(user.self)` -> results = `AttributeError: 'Person' object has no attribute 'self'`
    # `print(user.attribute_name)` -> results = content of attribute
