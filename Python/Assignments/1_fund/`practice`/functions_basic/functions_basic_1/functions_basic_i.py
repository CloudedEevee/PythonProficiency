#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#Prediction: 5     (correct)

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Prediction: Error, function requires arguments, was given none.
# Correct Answer: NameError: name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined
# I thought the function could be seen in the rest of the file, but could not. Therefore it was not yet defined. 

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Prediction: 5     (correct)


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Prediction: 5     (correct)


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Prediction: 5     (correct)   \n Error, variable not defined     (incorrect)
# Correct Answer: 
    # 5
    # None
# Variable IS defined (function), it just doesn't return anything so it's technically = None. 



#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# Prediction: 3  (correct)   \n  5 (correct)    \n  8   (incorrect)
# Correct Answer: 
    # 3
    # 5
    # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# The function doesn't return a value, just prints. The function technically = None and cannot be added together or concatinated.


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Prediction: 25     (correct)


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Prediction: 10   (incorrect)
# Correct Answer: 
    # 100
    # 10
# I didn't see the first print statement


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# Prediction: 7     (correct)
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prediction: 14     (correct)
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prediction: 21     (correct)


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Prediction: 8     (correct)


#11
b = 500
print(b)
# Prediction: 500     (correct)
def foobar():
    b = 300
    print(b)
print(b)
# Prediction: 500     (correct)
foobar()
# Prediction: 300     (correct)
print(b)
# Prediction: 500     (correct)


#12
b = 500
print(b)
# Prediction: 500     (correct)
def foobar():
    b = 300
    print(b)
    return b
print(b)
# Prediction: 500     (correct)
foobar()
# Prediction: 300     (correct)
print(b)
# Prediction: 500     (correct)


#13
b = 500
print(b)
# Prediction: 500     (correct)
def foobar():
    b = 300
    print(b)
    return b
print(b)
# Prediction: 500     (correct)
b=foobar()
# Prediction: 300     (correct)
print(b)
# Prediction: 300     (correct)


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Prediction: 1     (correct)
# Prediction: 3     (correct)
# Prediction: 2     (correct)


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
# Prediction: 1     (correct)
# Prediction: 3     (correct)
# Prediction: 5     (correct)
print(y)
# Prediction: 10     (correct)