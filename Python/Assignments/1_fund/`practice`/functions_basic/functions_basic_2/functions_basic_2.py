######################### Code Readability Setup #########################
separate = "##############################"
print(separate)

# The pattern: 
    # comment function purpose 
        # (I use these makeshift "labels" throughout my code to improve readability / understanding in the terminal)
    # set up a print for the function's label in terminal
    # define function
    # call function
    # separate function prints in terminal

############################## Functions ##############################

# Counts down from number given to 0, adds to list
print("The COUNTDOWN function prints:")
def countdown(start_num):
    count_list = []
    for num in range(start_num, 0, -1):
        count_list.append(num)
    print(count_list)
countdown(10)

print(separate)

# Give 2 numbers, print the first and return the second
def print_return(print_num, return_num):
    print("The PRINT_RETURN function prints:")
    print(print_num)
    return return_num
print(f"The PRINT_RETURN function returns: \n{print_return(5, 10)}")

print(separate)


# Give a list of numbers, return sum of the first value + length of list
print("The FIRST_PLUS_LENGTH function prints:")
def first_plus_length(num_list):
    print(num_list[0] + len(num_list))
my_num_list = [4,3,2,1,0]
first_plus_length(my_num_list)

print(separate)

# Give a list of numbers, create a new list of the values greater than the given list's second value, print new list length, return new list.
    # If given list is less than 2 values, return false
def greater_than_second_value(num_list):
    greater_than_second_list = []
    if len(num_list) < 2:
        return False
    
    for num in num_list:
        if num > num_list[1]:
            greater_than_second_list.append(num)
    print(f"The GREATER_THAN_SECOND_VALUE function prints: \n{len(greater_than_second_list)}")
    return greater_than_second_list
my_num_list = [1,2,3,4,5]
# my_num_list = [2,10,5,17,32,5,462,85,62,1,35,456,32,8,64,7,94,62,3,85,6,23,6,32]   # Different list than previous "my_num_list"
print(f"The GREATER_THAN_SECOND_VALUE function returns: \n{greater_than_second_value(my_num_list)}")

print(separate)

# Give 2 nums, first is for list length, second is for element values.
def length_value(list_length, value):
    function_list = []
    for num in range(list_length):
        function_list.append(value)
    return function_list
print(f"The LENGTH_VALUE function prints: \n{length_value(3,15)}")