# Variable declaration (also above)
# Data Types
    # Primitive
        # Boolean
boolean = True
        # Numbers
num1 = 42
num2 = 2.3
        # Strings
string = 'Hello World'
    # Composite
        # List 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
            # initialize
            # access value
            # change value
            # add value
            # delete value
        # Tuples
fruit = ('blueberry', 'strawberry', 'banana')
            # initialize
            # access value
        # Dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
            # initialize
            # access value
            # change value
            # add value
            # delete value



# Log statement
# Type Check
print(type(fruit))

print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])


# conditional
    # if
    # else if
    # else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# Length check
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop
    # start
    # stop
    # increment
    # break
    # continue
    # sequence
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)

# while loop
    # start
    # stop
    # increment
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)


# for loop
    # start
    # stop
    # increment
    # break
    # continue
    # sequence
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break


# function
    # parameter
    # argument
    # return
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
# Bonus: Errors

# NameError: name <variable name> is not defined
print(num3)
num3 = 72
# TypeError: 'tuple' object does not support item assignment
fruit[0] = 'cranberry'
# KeyError: 'favorite_team'
print(person['favorite_team'])
# IndexError: list index out of range
print(pizza_toppings[7])
# IndentationError: unexpected indent
  print(boolean)
# AttributeError: 'tuple' object has no attribute 'pop'
fruit.pop(1)
# AttributeError: 'tuple' object has no attribute 'append'
fruit.append('raspberry')
# Tuples
    # change value
    # add value
    # delete value